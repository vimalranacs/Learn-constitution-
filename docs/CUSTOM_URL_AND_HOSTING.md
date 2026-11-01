# Choose your own Constitution Atlas URL

You have two independent options.

## Keep the existing Sites deployment
The current URL is https://constitution-atlas-vimal.blondebarge1.chatgpt.site .
- To change its first label, choose the exact new slug (for example constitution-study). Sites provides a change_site_slug operation; it changes asynchronously and availability must be checked. The rest of the platform hostname remains platform-owned. No new label was guessed or applied.
- To use your own full domain (for example learn.your-domain.example), first own that domain and have access to its DNS. Sites provides add_custom_domain. It returns the exact CNAME or apex A records plus verification records. Add every returned record at the DNS provider, then refresh domain validation until verified. Do not invent DNS target addresses.
- You need to supply the desired slug or actual owned domain. No purchase or DNS change has been made.

## Host the portable application elsewhere
Use artifacts/constitution-atlas-universe and its README. This is standard Next.js on Node24 or Docker with persistent SQLite, not a Sites Worker. It does not require Cloudflare D1 or ChatGPT authentication.
1. Pick a host supporting a long-running Node process or Docker and a persistent disk. Static file hosts cannot run the AI server or saved-workspace API.
2. Install/build/start or deploy the supplied Dockerfile/compose file.
3. Set ATLAS_ORIGIN to the exact public origin (scheme, hostname and nonstandard port). Set GEMINI_API_KEY privately on that host and GEMINI_MODEL=gemini-3.1-flash-lite.
4. Mount persistent storage at ATLAS_DATABASE_PATH. Use a single instance with the SQLite adapter. Horizontal scaling/serverless deployments require a database adapter suited to that platform.
5. Connect your owned domain through the host's dashboard or reverse proxy and add only the DNS values provided there. Enable HTTPS.
6. Test without login: graph navigation, save/reload a note, resume a lesson and generate an AI summary.

The existing Sites secret does not transfer to a new host. You must enter it in that host's secret manager. No secret is included in exported source or archives. Reading and prepared content work without an AI key.

References: https://nextjs.org/docs/app/guides/self-hosting ; https://docs.docker.com/guides/nextjs/ .
