# Architecture decision

One React/TypeScript website and one Worker-compatible server boundary. Offline Python tools audit and export read-mostly knowledge; runtime requests never parse PDFs. Use canonical Argon IDs. Personal data belongs in D1 keyed by authenticated stable user ID, separately from knowledge records.

For the deployment spike, use Sites' supported Vinext React starter, retaining its Vite/Workers integration and server-side ChatGPT identity helper. This avoids a separate FastAPI hosting service and supplies an owner-private HTTPS deployment path. Initial private publication does not establish access for four friends. Confirm supported audience/membership policy before enabling them; never make the Site public to bypass that gate.

The scaffold has more dependencies than the desired eventual minimum. Retain the supported deployment setup for the spike; simplify only after successful build and deployment. Core content and Python tooling remain portable. A direct Cloudflare deployment would require a different verified identity boundary; forwarded identity headers must never be trusted on an exposed origin.

## Alternatives and constraints checked

- Old React + separate FastAPI: preserves code but introduces two hosting surfaces and mutable SQLite persistence risks. Keep FastAPI as an offline baseline rather than production.
- Static-only site: cannot enforce app-level private records or safely proxy Gemini. Rejected for the final application.
- Direct Cloudflare Workers + D1: practical alternative pending account/auth setup. Official pages checked 2026-11-01: Workers Free 100,000 requests/day, 10 ms CPU/request; D1 Free 5 million rows read/day, 100,000 written/day, 5 GB total. These provider figures do not establish Sites account entitlements or promise unlimited free usage.

References: https://developers.cloudflare.com/workers/platform/limits/ ; https://developers.cloudflare.com/workers/platform/pricing/ ; https://developers.cloudflare.com/d1/platform/pricing/ . Recheck before direct deployment. Do not enable paid plans or services.

## Dependency sequence

Preservation → source-aware import → first API/Atlas/lesson → private deploy and UI QA → identity-scoped persistence → richer graph and first complete course → AI and advanced scenarios. Security starts early; full access/isolation acceptance remains explicit.
