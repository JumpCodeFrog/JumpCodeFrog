<p align="center"><img width="880" alt="Thomas Rosenstein — Go and C++ engineer, HFT, DevOps, Moscow. Terminal showing uname, the uring-kv process, a benchmark of 181,553 requests per second, and the role line." src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/main/banner-boot.svg" /></p>

I'm Thomas Rosenstein, a Go and C++ engineer in Moscow. I work on low-latency backends and the
infrastructure that keeps them up — kernel-side I/O, single-binary services, and the unglamorous
operational half that decides whether any of it survives contact with production.

The four repositories below are the public evidence. **[uring-kv](https://github.com/JumpCodeFrog/uring-kv)**
is the one to read first: an async TCP key-value server where `accept`, `recv` and `send` are all
submitted through `io_uring`, with no epoll and no blocking syscall on the hot path.

---

## `$ whoami`

```
┌─ operator ───────────────────────────────────────────────┐
│ handle     @JumpCodeFrog                                 │
│ org        ThomasRosen inc.                              │
│ works in   Go · C++20 · Python · Linux                   │
├─ account ────────────────────────────────────────────────┤
│ joined     2024-06-19                                    │
│ public     6 repositories   (all four real ones below)   │
│ private    8 repositories   (summarised, not detailed)   │
└──────────────────────────────────────────────────────────┘
```

I write two kinds of software. The first lives on a hot path, where the interesting question is *which syscalls you didn't make*. The second is boring on purpose: one static binary, one job, a changelog, and a release someone else can actually install.

Everything on this page is either readable in a public repo or explicitly marked as an unverifiable claim. **No uptime figures, no throughput charts, no latency numbers offered as measured results** — I haven't published those benchmarks, so I won't quote them at you.

---

## `$ ls -l ~/public`

<p align="center"><a href="https://github.com/JumpCodeFrog/uring-kv"><img width="880" alt="uring-kv: async TCP key-value server on io_uring. ASCII schematic of submission queue, kernel and completion queue. C++20, MIT, Linux 5.10+, 31 KB of C++. Open repository." src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/main/card-uring-kv-amber.svg" /></a></p>
<p align="center"><a href="https://github.com/JumpCodeFrog/telegram-shop-bot"><img width="880" alt="telegram-shop-bot: open-source Telegram storefront in Go. ASCII receipt for an order paid via Telegram Stars. Single static binary, CGO off, SQLite embedded. MIT, v1.2.0. Open repository." src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/main/card-telegram-shop-bot.svg" /></a></p>
<p align="center"><a href="https://github.com/JumpCodeFrog/aipf"><img width="880" alt="aipf: API Proxy Forensics Toolkit. ASCII probe battery covering the model list, streaming, retry behaviour, wrapper leaks and provider identity. Async Python CLI, MIT. Open repository." src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/main/card-aipf.svg" /></a></p>
<p align="center"><a href="https://github.com/JumpCodeFrog/go-market-watcher"><img width="880" alt="go-market-watcher: CLI price watcher. ASCII chart of a price history series. Go 1.25, PostgreSQL 16, Docker Compose, MIT. Open repository." src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/main/card-go-market-watcher.svg" /></a></p>

<sub><b>Also public:</b> <a href="https://github.com/JumpCodeFrog/dpowcoin">dpowcoin</a> — a Bitcoin Core-derived C++ fork. The overwhelming bulk of that tree is upstream, not my code; it inflates my C++ line count and proves nothing about me, so it is excluded from the language panel below. And <a href="https://github.com/JumpCodeFrog/JumpCodeFrog">JumpCodeFrog</a>, the repository that draws this page — every panel on it is an SVG built here, not a call to somebody else's service.</sub>

---

## `$ stack --installed --diff-from-cards`

<p align="center"><img width="880" alt="Also in the toolbox, beyond what the four cards above already show: Rust, PHP, systemd, GitHub Actions, goreleaser and golangci-lint." src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/main/strip-stack.svg" /></p>

---

<details>
<summary><b><code>$ ls ~/private --summary</code></b> &mdash; eight private repositories, named but not offered as evidence</summary>
<br>
<p>Eight private repositories, all of them listed below &mdash; the count and the names, so this section cannot be read as hinting at more than exists. <b>Everything here is my own description of code you cannot open from this profile.</b> Weigh it accordingly; the public repositories above are the evidence.</p>
<table>
<tr><td><b>shitproxy</b></td><td><code>Go</code></td><td>LLM gateway translating between the OpenAI and Anthropic API shapes. <code>aipf</code> is the auditing half of the same problem, published because the auditing half is the half that's safe to publish.</td></tr>
<tr><td><b>shitproxy-channels-backup</b></td><td><code>&mdash;</code></td><td>Automated backup of the gateway's channel and token config, on a 6-hour cycle.</td></tr>
<tr><td><b>pupa-backend</b></td><td><code>Go</code></td><td>Backend service: auth, OTP over a smart identifier, Swagger/OpenAPI-documented surface.</td></tr>
<tr><td><b>my_coin</b></td><td><code>Rust</code></td><td>No published description. Listed as the source of the Rust in the toolbox row.</td></tr>
<tr><td><b>x-plata</b></td><td><code>PHP</code></td><td>No published description.</td></tr>
<tr><td><b>ru.repair</b> &middot; <b>siteforcompany</b> &middot; <b>workspacerurepair</b></td><td><code>PHP</code></td><td>Earlier commercial web work. Where the PHP in the toolbox row comes from, and the reason it is listed there rather than up top.</td></tr>
</table>
<p><sub>The trading work in my bio is closed and not in a repository on this account, so there is nothing here to point you at and no benchmark of it I can publish. Judge the systems claim on <code>uring-kv</code> instead &mdash; that one is public, it is mine, and it is 31 KB of C++.</sub></p>
</details>

<details>
<summary><b><code>$ activity --topology</code></b> &mdash; contribution and language panels, rebuilt daily by this repository</summary>
<br>
<p align="center"><img width="430" alt="Repository and activity metrics for JumpCodeFrog, generated as a static SVG by a scheduled Action in this repository." src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/main/metrics-overview.svg" /> <img width="430" alt="Most-used languages across JumpCodeFrog's repositories, with the dpowcoin fork excluded so that upstream Bitcoin Core C++ does not dominate the chart." src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/main/metrics-languages.svg" /></p>
<p align="center"><picture><source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/output/github-contribution-grid-snake-dark.svg" /><source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/output/github-contribution-grid-snake.svg" /><img width="880" alt="Contribution grid for JumpCodeFrog, drawn as a snake eating the commit squares, in the amber palette." src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/output/github-contribution-grid-snake.svg" /></picture></p>
<p><sub>The metrics and language panels are <b>static SVGs</b>, rebuilt daily by a scheduled Action in this repository and committed to <code>main</code>; the snake is rebuilt the same way onto the <code>output</code> branch. Nothing among them is computed by a third party at page load. The language panel excludes <code>dpowcoin</code> for the reason given above.</sub></p>
</details>

---

## `$ how-i-work`

- **Read the syscalls, then the code.** `strace`, `perf` and a flamegraph settle arguments that opinions don't.
- **Delete the fallback.** Two code paths means one of them is untested. Pick the target platform and say so in the README.
- **Boring deploys.** Static binary, CGO off, embedded storage by default, optional dependencies actually optional.
- **Ship the paperwork.** CI, lint, changelog, security policy.
- **Small blast radius.** `aipf` has no server. `uring-kv` has no framework. Scope is a feature.

---

<p align="center"><img width="880" alt="Contact: Telegram at thomasrosenstain, email thomasrosenstain at gmail dot com. Issues and pull requests on any public repository get read." src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/main/block-contact.svg" /></p>
<p align="center"><img width="880" alt="Section divider" src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/main/rule.svg" /></p>
