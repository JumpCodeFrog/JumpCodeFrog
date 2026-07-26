<div align="center">

<img alt="Thomas Rosenstein — Go and C++ Engineer · HFT · DevOps · Moscow" src="https://capsule-render.vercel.app/api?type=rect&color=00FF41&height=120&section=header&text=Thomas%20Rosenstein&fontSize=42&fontColor=0D0D0D&fontAlignY=44&desc=Go%20%26%20C%2B%2B%20Engineer%20%C2%B7%20HFT%20%C2%B7%20DevOps%20%C2%B7%20Moscow&descSize=16&descAlignY=72&descColor=0D0D0D" />

<a href="https://github.com/JumpCodeFrog?tab=repositories">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=17&duration=3400&pause=900&color=00FF41&background=00000000&center=true&vCenter=true&width=720&lines=uring-kv+%E2%80%94+async+TCP+KV+server+on+io_uring%2C+no+epoll;telegram-shop-bot+%E2%80%94+one+static+Go+binary%2C+CGO+off;aipf+%E2%80%94+async+forensics+CLI+for+LLM+proxy+APIs;go-market-watcher+%E2%80%94+Go+1.25+%2B+PostgreSQL+16+%2B+Compose" />
  <source media="(prefers-color-scheme: light)" srcset="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=17&duration=3400&pause=900&color=15803D&background=00000000&center=true&vCenter=true&width=720&lines=uring-kv+%E2%80%94+async+TCP+KV+server+on+io_uring%2C+no+epoll;telegram-shop-bot+%E2%80%94+one+static+Go+binary%2C+CGO+off;aipf+%E2%80%94+async+forensics+CLI+for+LLM+proxy+APIs;go-market-watcher+%E2%80%94+Go+1.25+%2B+PostgreSQL+16+%2B+Compose" />
  <img alt="uring-kv — async TCP KV server on io_uring, no epoll · telegram-shop-bot — one static Go binary, CGO off · aipf — async forensics CLI for LLM proxy APIs · go-market-watcher — Go 1.25 + PostgreSQL 16 + Compose" src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=17&duration=3400&pause=900&color=15803D&background=00000000&center=true&vCenter=true&width=720&lines=uring-kv+%E2%80%94+async+TCP+KV+server+on+io_uring%2C+no+epoll" />
</picture>
</a>

<a href="https://t.me/thomasrosenstain"><img alt="Telegram @thomasrosenstain" src="https://img.shields.io/badge/Telegram-%40thomasrosenstain-00FF41?style=for-the-badge&logo=telegram&logoColor=00FF41&labelColor=0D0D0D" /></a>
<a href="mailto:thomasrosenstain@gmail.com"><img alt="Email thomasrosenstain@gmail.com" src="https://img.shields.io/badge/Email-thomasrosenstain-00FF41?style=for-the-badge&logo=gmail&logoColor=00FF41&labelColor=0D0D0D" /></a>
<a href="https://github.com/JumpCodeFrog?tab=repositories"><img alt="Public repositories" src="https://img.shields.io/badge/Public%20repos-6-00FF41?style=for-the-badge&logo=github&logoColor=00FF41&labelColor=0D0D0D" /></a>

</div>

---

## `$ whoami`

```
┌─ operator ───────────────────────────────────────────────┐
│ name       Thomas Rosenstein                             │
│ handle     @JumpCodeFrog                                 │
│ org        ThomasRosen inc.                              │
│ location   Moscow, RU                                    │
│ works in   Go · C++20 · Python · Linux                   │
│ domain     low-latency systems · trading infra · DevOps  │
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

<table>
<tr>
<td width="50%" valign="top">

<h3><a href="https://github.com/JumpCodeFrog/uring-kv">uring-kv</a></h3>

<p><b>Async TCP key-value server built entirely on <code>io_uring</code>.</b> <code>accept</code>, <code>recv</code> and <code>send</code> are all submitted through the ring. No epoll, no Boost, no blocking syscall on the hot path — the event loop's only wait is on completions.</p>

<p>
<img alt="C++20" src="https://img.shields.io/badge/C%2B%2B20-00FF41?style=flat-square&logo=cplusplus&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="liburing" src="https://img.shields.io/badge/liburing-00FF41?style=flat-square&labelColor=0D0D0D" />
<img alt="CMake" src="https://img.shields.io/badge/CMake-00FF41?style=flat-square&logo=cmake&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="Linux 5.10+" src="https://img.shields.io/badge/Linux%205.10%2B-00FF41?style=flat-square&logo=linux&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="MIT" src="https://img.shields.io/badge/MIT-00FF41?style=flat-square&labelColor=0D0D0D" />
</p>

<p><sub>Plain-text line protocol over TCP, so <code>nc</code> is a valid client · <code>README.md</code> + <code>README.ru.md</code></sub></p>

<p><sub><b>Start here.</b> 31 KB of C++ — small enough to audit the design in one sitting, which is the point. This is the public artifact behind the low-latency line in my bio. Read the loop, not the adjectives.</sub></p>

</td>
<td width="50%" valign="top">

<h3><a href="https://github.com/JumpCodeFrog/telegram-shop-bot">telegram-shop-bot</a></h3>

<p><b>A complete Telegram storefront in Go.</b> Catalog, cart, Telegram Stars and USDT payments, promo codes, admin panel, i18n locales. SQLite is embedded and the build is CGO-free, so the whole shop ships as one binary you can <code>scp</code> to a VPS. Redis is optional, not assumed.</p>

<p>
<img alt="Go" src="https://img.shields.io/badge/Go-00FF41?style=flat-square&logo=go&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="SQLite embedded" src="https://img.shields.io/badge/SQLite%20embedded-00FF41?style=flat-square&logo=sqlite&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="Redis optional" src="https://img.shields.io/badge/Redis%20optional-00FF41?style=flat-square&logo=redis&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="Docker" src="https://img.shields.io/badge/Docker-00FF41?style=flat-square&logo=docker&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="MIT" src="https://img.shields.io/badge/MIT%20%C2%B7%20v1.2.0-00FF41?style=flat-square&labelColor=0D0D0D" />
</p>

<p><sub>Telegram Bot API v5 · CI · golangci-lint · goreleaser · CHANGELOG · CONTRIBUTING · SECURITY.md · <code>monitoring/</code></sub></p>

<p><sub><b>Shipped, not demoed.</b> The paperwork is the difference between a repo and a project. A payments bot with no disclosure address is an unfinished payments bot.</sub></p>

</td>
</tr>
<tr>
<td width="50%" valign="top">

<h3><a href="https://github.com/JumpCodeFrog/aipf">aipf</a></h3>

<p><b>API Proxy Forensics Toolkit.</b> An async CLI that points a probe battery at OpenAI/Anthropic-compatible LLM proxies and emits a structured JSON report, redacted logs, and sanitized capture/replay — so the artifact is safe to paste into a ticket.</p>

<p>
<img alt="Python 3.11+" src="https://img.shields.io/badge/Python%203.11%2B-00FF41?style=flat-square&logo=python&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="pytest" src="https://img.shields.io/badge/pytest-00FF41?style=flat-square&logo=pytest&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="ruff" src="https://img.shields.io/badge/ruff-00FF41?style=flat-square&labelColor=0D0D0D" />
<img alt="mypy" src="https://img.shields.io/badge/mypy-00FF41?style=flat-square&labelColor=0D0D0D" />
<img alt="MIT" src="https://img.shields.io/badge/MIT-00FF41?style=flat-square&labelColor=0D0D0D" />
</p>

<p><sub>Probe battery · structured JSON reports · redacted logs · sanitized capture/replay</sub></p>

<p><sub><b>The design decision is what it isn't.</b> No server, no database, no UI. A forensics tool that needs its own deployment is a tool nobody reaches for at the moment they need it.</sub></p>

</td>
<td width="50%" valign="top">

<h3><a href="https://github.com/JumpCodeFrog/go-market-watcher">go-market-watcher</a></h3>

<p><b>CLI price watcher for Wildberries.</b> Search, price history into PostgreSQL, CSV export, proxy rotation, the whole thing up on Docker Compose.</p>

<p>
<img alt="Go 1.25" src="https://img.shields.io/badge/Go%201.25-00FF41?style=flat-square&logo=go&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="PostgreSQL 16" src="https://img.shields.io/badge/PostgreSQL%2016-00FF41?style=flat-square&logo=postgresql&logoColor=00FF41&labelColor=0D0D0D" />
<img alt="Docker Compose" src="https://img.shields.io/badge/Compose-00FF41?style=flat-square&logo=docker&logoColor=00FF41&labelColor=0D0D0D" />
</p>

<p><sub>Unit tests cover the parser and proxy packages — the two places a scraper actually rots when the marketplace changes.</sub></p>

<p><sub><b>Fair warning while you're reading it:</b> no LICENSE file on this one yet. That's an oversight, not a position — treat it as all-rights-reserved until I fix it.</sub></p>

</td>
</tr>
</table>

<sub><b>Also public:</b> <a href="https://github.com/JumpCodeFrog/dpowcoin">dpowcoin</a> — a Bitcoin Core-derived C++ fork. Listed for completeness and labelled honestly: the overwhelming bulk of that tree is upstream Bitcoin Core, not my code. It inflates my C++ line count and proves nothing about me, so it is excluded from the language chart below. Judge the C++ on <code>uring-kv</code> instead — that one is 31 KB and all of it is mine.</sub>

<details>
<summary><b>&nbsp;Why completion-based I/O, in the shape it actually takes</b></summary>

<br>

```cpp
// Readiness (epoll): kernel says "you may read now" -> you syscall -> maybe EAGAIN.
// Completion (io_uring): you say "read this" -> kernel says "it is done, here is the result".

static void submit_recv(io_uring* ring, Conn* c) {
    io_uring_sqe* sqe = io_uring_get_sqe(ring);          // slot in the submission queue
    if (!sqe) { c->defer_recv(); return; }               // ring full: re-queue, never block to make room
    io_uring_prep_recv(sqe, c->fd, c->buf.data(), c->buf.size(), 0);
    io_uring_sqe_set_data(sqe, c);                       // completion carries the connection back
}

// Single-threaded loop. One enter into the kernel per batch, not per socket.
for (;;) {
    io_uring_submit_and_wait(&ring, 1);                  // the only place we ever block

    unsigned head, seen = 0;
    io_uring_cqe* cqe;
    io_uring_for_each_cqe(&ring, head, cqe) {
        auto* c = static_cast<Conn*>(io_uring_cqe_get_data(cqe));
        c->on_complete(cqe->res);                        // res < 0  =>  -errno, no errno global
        ++seen;
    }
    io_uring_cq_advance(&ring, seen);                    // batch-ack the whole drain
}
```

<sub><i>Illustrative sketch of the pattern, written for this page — not a copy of the repository source. Clone the repo for the real thing.</i></sub>

Why I keep choosing this shape:

- **The connection object rides in the completion.** `io_uring_sqe_set_data` / `io_uring_cqe_get_data` means there is no fd → state lookup on the hot path. The state finds you.
- **Errors are values, not `errno`.** `cqe->res` is a negative errno on failure. No thread-local read, no ordering hazard between "the call failed" and "why it failed".
- **One kernel transition per batch.** `io_uring_submit_and_wait` submits everything queued and waits once. Under load the ratio of useful work to syscalls goes the right way on its own.
- **`io_uring_cq_advance` after a full drain**, not `cqe_seen` per entry — one store instead of N.
- **No fallback path.** An epoll backend would double the state machine and halve how much I trust it. Linux 5.10+ is a documented requirement instead.

The design intent is the lowest response latency the kernel will give me on this shape. That is a goal, not a published measurement — there is no benchmark in the repo, so treat it as the reason for the architecture rather than a result you can cite.

</details>

---

## `$ ls ~/private --summary`

Eight private repositories. I'm flagging the boundary rather than blurring it: **everything in this section is my own description of private work, not something you can verify from this profile.** Weigh it accordingly — the public repos above are the evidence.

<table>
<tr><td><b>BingX HFT bot</b></td><td><code>Go</code></td><td>Trading system. <i>My description, unverifiable from here:</i> ONNX Runtime inference in the decision path, a 32-factor indicator engine, sub-millisecond execution. No public benchmark backs that last phrase. If you want to check whether I can write that kind of I/O loop, read <code>uring-kv</code> — same discipline, public.</td></tr>
<tr><td><b>shitproxy</b></td><td><code>Go</code></td><td>LLM gateway translating between the OpenAI and Anthropic API shapes. <code>aipf</code> is the auditing half of the same problem, published because the auditing half is safe to publish.</td></tr>
<tr><td><b>pupa-backend</b></td><td><code>Go</code></td><td>Backend service: auth, OTP, Swagger/OpenAPI-documented surface.</td></tr>
<tr><td><b>my_coin</b></td><td><code>Rust</code></td><td>Private, no published description. Listed as the source of the Rust below.</td></tr>
<tr><td><b>x-plata</b></td><td><code>PHP</code></td><td>Private, no published description. Listed as the source of the PHP below.</td></tr>
</table>

---

## `$ stack --installed`

<div align="center">

[![Stack](https://skillicons.dev/icons?i=go,cpp,rust,python,php,linux,docker,postgres,sqlite,redis,cmake,grafana,git,githubactions&perline=7&theme=dark)](https://github.com/JumpCodeFrog?tab=repositories)

<sub>Every icon maps to something committed in a repository on this account, public or private. Nothing is listed aspirationally.</sub>

</div>

---

## `$ activity --topology`

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/output/github-contribution-grid-snake.svg" />
  <img alt="Contribution grid snake animation" src="https://raw.githubusercontent.com/JumpCodeFrog/JumpCodeFrog/output/github-contribution-grid-snake-dark.svg" />
</picture>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=JumpCodeFrog&theme=github-dark-blue&hide_border=true&border_radius=8&ring=00FF41&fire=00FF41&currStreakLabel=00FF41" />
  <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com?user=JumpCodeFrog&theme=default&hide_border=true&border_radius=8" />
  <img alt="Contribution streak for JumpCodeFrog" src="https://streak-stats.demolab.com?user=JumpCodeFrog&hide_border=true&border_radius=8" width="58%" />
</picture>

<br><br>

<sub>Both panels are generated from GitHub's own contribution history. The snake is a <b>static SVG</b> rebuilt by a scheduled Action in this repository and committed to its <code>output</code> branch — no third-party service computes it at page load.</sub>

</div>

---

## `$ how-i-work`

- **Read the syscalls, then the code.** `strace`, `perf` and a flamegraph settle arguments that opinions don't.
- **Delete the fallback.** Two code paths means one of them is untested. Pick the target platform and say so in the README.
- **Boring deploys.** Static binary, CGO off, embedded storage by default, optional dependencies actually optional.
- **Ship the paperwork.** CI, lint, changelog, security policy.
- **Small blast radius.** `aipf` has no server. `uring-kv` has no framework. Scope is a feature.

---

<div align="center">

<a href="https://t.me/thomasrosenstain"><img alt="Telegram @thomasrosenstain" src="https://img.shields.io/badge/Telegram-%40thomasrosenstain-00FF41?style=for-the-badge&logo=telegram&logoColor=00FF41&labelColor=0D0D0D" /></a>
<a href="mailto:thomasrosenstain@gmail.com"><img alt="Email thomasrosenstain@gmail.com" src="https://img.shields.io/badge/Email-thomasrosenstain%40gmail.com-00FF41?style=for-the-badge&logo=gmail&logoColor=00FF41&labelColor=0D0D0D" /></a>

<sub><b>ThomasRosen inc.</b> · Moscow, RU · Low-latency backends, trading infrastructure, systems work.<br>
Issues and PRs on any public repo above are read. Best first message: name the syscall you're worried about.</sub>

<img alt="" src="https://capsule-render.vercel.app/api?type=rect&color=00FF41&height=6&section=footer" />

</div>
