#!/usr/bin/env python3
"""Generate the public language card without a user-scoped GitHub token."""

from __future__ import annotations

import argparse
import html
import json
import os
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence

API_ROOT = "https://api.github.com"
DEFAULT_USER = "JumpCodeFrog"
DEFAULT_SKIPPED_REPOSITORIES = frozenset({"dpowcoin"})
MAX_LANGUAGES = 8
MIN_PERCENT = 1.0

LANGUAGE_COLORS = {
    "C": "#555555",
    "C#": "#178600",
    "C++": "#f34b7d",
    "CSS": "#663399",
    "Dart": "#00B4AB",
    "Dockerfile": "#384d54",
    "Go": "#00ADD8",
    "HTML": "#e34c26",
    "Java": "#b07219",
    "JavaScript": "#f1e05a",
    "Jupyter Notebook": "#DA5B0B",
    "Kotlin": "#A97BFF",
    "Lua": "#000080",
    "PHP": "#4F5D95",
    "PowerShell": "#012456",
    "Python": "#3572A5",
    "Ruby": "#701516",
    "Rust": "#dea584",
    "Shell": "#89e051",
    "Swift": "#F05138",
    "TypeScript": "#3178c6",
    "Vue": "#41b883",
}
FALLBACK_COLORS = (
    "#FFB000",
    "#D59D53",
    "#B47F40",
    "#A67637",
    "#E8A33D",
    "#C07E1E",
    "#8C5E22",
    "#FFE2AE",
)

JsonFetcher = Callable[[str], Any]


def fetch_json(url: str) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "JumpCodeFrog-profile-metrics",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_public_repositories(user: str, fetcher: JsonFetcher = fetch_json) -> list[Mapping[str, Any]]:
    repositories: list[Mapping[str, Any]] = []
    page = 1
    while True:
        query = urllib.parse.urlencode(
            {"type": "owner", "sort": "full_name", "per_page": 100, "page": page}
        )
        batch = fetcher(f"{API_ROOT}/users/{urllib.parse.quote(user)}/repos?{query}")
        if not isinstance(batch, list):
            raise RuntimeError("GitHub repositories response was not a list")
        repositories.extend(batch)
        if len(batch) < 100:
            return repositories
        page += 1


def collect_language_bytes(
    repositories: Iterable[Mapping[str, Any]],
    fetcher: JsonFetcher = fetch_json,
    skipped_repositories: frozenset[str] = DEFAULT_SKIPPED_REPOSITORIES,
) -> tuple[dict[str, int], int]:
    totals: defaultdict[str, int] = defaultdict(int)
    repository_count = 0

    for repository in repositories:
        name = str(repository.get("name", ""))
        if (
            not name
            or repository.get("private")
            or repository.get("fork")
            or name.lower() in skipped_repositories
        ):
            continue

        languages_url = repository.get("languages_url")
        if not isinstance(languages_url, str) or not languages_url:
            continue

        repository_count += 1
        languages = fetcher(languages_url)
        if not isinstance(languages, Mapping):
            raise RuntimeError(f"Languages response for {name} was not an object")
        for language, byte_count in languages.items():
            if isinstance(language, str) and isinstance(byte_count, int) and byte_count > 0:
                totals[language] += byte_count

    return dict(totals), repository_count


def summarize_languages(
    totals: Mapping[str, int],
    limit: int = MAX_LANGUAGES,
    minimum_percent: float = MIN_PERCENT,
) -> list[tuple[str, int, float]]:
    total_bytes = sum(totals.values())
    if total_bytes <= 0:
        raise RuntimeError("No public language data was returned; refusing to publish an empty card")

    summary = [
        (language, byte_count, byte_count * 100.0 / total_bytes)
        for language, byte_count in totals.items()
        if byte_count > 0
    ]
    summary.sort(key=lambda item: (-item[1], item[0].casefold()))
    return [item for item in summary if item[2] >= minimum_percent][:limit]


def language_color(language: str, index: int) -> str:
    return LANGUAGE_COLORS.get(language, FALLBACK_COLORS[index % len(FALLBACK_COLORS)])


def compact_name(language: str, maximum: int = 20) -> str:
    return language if len(language) <= maximum else f"{language[: maximum - 1]}…"


def render_svg(
    summary: Sequence[tuple[str, int, float]],
    total_language_count: int,
    repository_count: int,
    user: str = DEFAULT_USER,
) -> str:
    if not summary:
        raise RuntimeError("Cannot render an empty language summary")

    width = 480
    height = 196
    bar_x = 20.0
    bar_width = 440.0
    cumulative_x = bar_x
    segments: list[str] = []
    rows: list[str] = []

    displayed_percent = sum(item[2] for item in summary)
    for index, (language, _byte_count, percent) in enumerate(summary):
        color = language_color(language, index)
        segment_width = bar_width * percent / 100.0
        if index == len(summary) - 1:
            segment_width = max(0.0, bar_width * displayed_percent / 100.0 - (cumulative_x - bar_x))
        segments.append(
            f'<rect x="{cumulative_x:.2f}" y="58" width="{segment_width:.2f}" height="10" fill="{color}"/>'
        )
        cumulative_x += segment_width

        sparse_layout = len(summary) <= 4
        column = 0 if sparse_layout else index // 4
        row = index if sparse_layout else index % 4
        x = 20 + column * 228
        percentage_x = 460 if sparse_layout else x + 210
        y = 95 + row * 22
        safe_name = html.escape(compact_name(language, 34 if sparse_layout else 20))
        rows.append(
            f'<rect x="{x}" y="{y - 9}" width="9" height="9" rx="2" fill="{color}"/>'
            f'<text x="{x + 16}" y="{y}" font-size="12" fill="#FFE2AE">{safe_name}</text>'
            f'<text x="{percentage_x}" y="{y}" text-anchor="end" font-size="11.5" fill="#D59D53">{percent:.2f}%</text>'
        )

    safe_user = html.escape(user)
    aria_label = html.escape(
        f"{total_language_count} languages across {repository_count} public repositories for {user}. "
        "The upstream-heavy dpowcoin fork is excluded."
    )
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" role="img" aria-label="{aria_label}" font-family="ConsolasFallback,ui-monospace,SFMono-Regular,Menlo,'DejaVu Sans Mono',monospace">
<title>Public language usage for {safe_user}</title>
<style>@font-face{{src:local('Consolas'),local('DejaVu Sans Mono');font-family:ConsolasFallback;font-display:swap;size-adjust:105%}}</style>
<defs><filter id="g" x="-25%" y="-70%" width="150%" height="240%"><feGaussianBlur stdDeviation="1.1" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter><pattern id="s" width="4" height="4" patternUnits="userSpaceOnUse"><rect width="4" height="1" fill="#000" opacity=".3"/></pattern><radialGradient id="v"><stop offset="60%" stop-color="#000" stop-opacity="0"/><stop offset="100%" stop-color="#000" stop-opacity=".64"/></radialGradient><clipPath id="bar"><rect x="20" y="58" width="440" height="10" rx="5"/></clipPath></defs>
<rect width="480" height="196" rx="4" fill="#0D0804"/>
<rect width="480" height="32" rx="4" fill="#1A1007"/>
<text x="18" y="22" font-size="13" font-weight="700" fill="#FFB000" filter="url(#g)">{total_language_count} LANGUAGES</text>
<text x="462" y="22" text-anchor="end" font-size="10.5" fill="#A67637">PUBLIC REPOSITORIES · DPOWCOIN EXCLUDED</text>
<text x="20" y="49" font-size="11.5" fill="#D59D53">most-used by GitHub language bytes</text>
<g clip-path="url(#bar)"><rect x="20" y="58" width="440" height="10" fill="#2F1F0E"/>{''.join(segments)}</g>
{''.join(rows)}
<path d="M20 178H460" stroke="#4E3517"/>
<text x="20" y="191" font-size="9.5" fill="#A67637">{repository_count} PUBLIC NON-FORK REPOSITORIES · GENERATED BY REPOSITORY-SCOPED GITHUB_TOKEN</text>
<rect width="480" height="196" rx="4" fill="url(#s)"/><rect width="480" height="196" rx="4" fill="url(#v)"/><rect x=".5" y=".5" width="479" height="195" rx="4" fill="none" stroke="#7A511B"/>
</svg>
'''
    ET.fromstring(svg)
    return svg


def generate(user: str, output: Path, fetcher: JsonFetcher = fetch_json) -> tuple[int, int]:
    repositories = fetch_public_repositories(user, fetcher)
    totals, repository_count = collect_language_bytes(repositories, fetcher)
    summary = summarize_languages(totals)
    svg = render_svg(summary, len(totals), repository_count, user)
    output.write_text(svg, encoding="utf-8")
    return len(totals), repository_count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--user", default=DEFAULT_USER)
    parser.add_argument("--output", type=Path, default=Path("metrics-languages.svg"))
    args = parser.parse_args()
    language_count, repository_count = generate(args.user, args.output)
    print(f"Generated {args.output}: {language_count} languages across {repository_count} public repositories")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
