# Constitution Atlas — deploy on your own host

This is a standalone Next.js/Node application, independent of Sites, Cloudflare D1 and ChatGPT sign-in. Anyone can read it. A random HttpOnly browser cookie separates saved notes/progress; this is device storage, not an authenticated account. Do not use shared browser profiles for sensitive notes. Old Sites account data is not copied or exposed.

## Node server
Install Node 24 LTS (minimum 22.13). In this folder run `npm install`, `npm run build`, then `npm start`. The server listens on port 3000. Set environment variables in your host's secret settings or a local `.env.local` file:

```
GEMINI_API_KEY=your-own-secret-key
ATLAS_ORIGIN=https://your-actual-domain.example
GEMINI_MODEL=gemini-3.1-flash-lite
ATLAS_DATABASE_PATH=/persistent-data/atlas.sqlite
```

The API key already configured in Sites does **not** travel with this export. Set it once on your new host. Do not put it in NEXT_PUBLIC variables, Git or frontend code. If a key was shared publicly, replace it in Google AI Studio and update the server secret.

SQLite is created on first personal-data request. Mount a persistent disk at its parent directory. Use one application instance with this SQLite setup. Ephemeral/serverless filesystems lose changes; multiple instances require a shared database adapter. Static-only hosting cannot run the AI proxy or saved workspaces.

## Docker
Create a `.env` containing the Gemini variables above (optional for reading). Run `docker compose up --build -d`. The supplied volume keeps `/data/atlas.sqlite` through container restarts. Use your hosting provider's HTTPS reverse proxy in front of port 3000. Keep the persistent volume and secret settings during updates. Back up the SQLite database while the app is stopped, or use SQLite's backup API while running.

## Choose your own URL
1. Buy or use a domain you control. The app's source does not hard-code the Sites URL.
2. Deploy this app on a Node/Docker host with persistent disk, or a VPS.
3. Add the domain in that host's dashboard. Copy the exact DNS records it supplies (usually CNAME for a subdomain, A/AAAA for a VPS). Do not guess values.
4. Add those records at your DNS provider. Enable the host's HTTPS certificate and wait for it to become active.
5. Test the new HTTPS domain: reading, graph controls, a saved note after reload, and an AI summary. Ensure the reverse proxy forwards the original Host header so same-origin API checks work.

For a VPS, a reverse proxy such as Caddy can serve `your-domain.example` and proxy to `127.0.0.1:3000`. Substitute only your actual domain, point DNS to that server and open ports 80/443. You must configure your domain, DNS, hosting account and server secrets manually; no domain has been purchased or configured for you.

## AI behavior
The tutor gets the active entity or exact lesson section, depth/language, and the last four exchanges. Summary/explanation/example/quiz actions use that same context. It cannot know unrelated tabs or material you have not supplied. Limits are 30 calls per browser/account and 150 site-wide per UTC day. Changing cookies does not evade the shared site-wide budget. These app limits do not replace Google billing controls. Reading works without a key, with retrieved source suggestions in place of generated answers.

## Sources and maintenance
Read `/methodology`. Supplied curriculum and graph claims are not all independently reviewed. Keep the source, lockfile and database backups. Node/Docker support follows Next.js self-hosting: https://nextjs.org/docs/app/guides/self-hosting and https://nodejs.org/api/sqlite.html .
