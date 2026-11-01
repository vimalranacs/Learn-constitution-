# Local development (Windows PowerShell)

Run from the workspace root. Prerequisites: Python 3.10+ (supplied venv is Python 3.13), Node 22.13+ and Git. Original files are preserved under the nested legacy directory.

```powershell
python tools/audit_legacy.py
python -m unittest discover -s tests -v
& './constitution_atlas_fullstack/constitution_atlas_fullstack/backend/venv/Scripts/python.exe' './constitution_atlas_fullstack/constitution_atlas_fullstack/tests/test_constitution_atlas.py'
& './constitution_atlas_fullstack/constitution_atlas_fullstack/backend/venv/Scripts/python.exe' tools/import_first_slice.py --pdf 'C:\Users\Vimal rana\Downloads\88cca69e868e50b217f855be2fb8bdba.pdf'
cd atlas-web
npm.cmd run install:ci
npm.cmd run dev
```

If the supplied venv is unavailable, create a fresh `.venv` and install the preserved backend requirements into it; do not overwrite the legacy venv or run the legacy ingestion entry point. The new importer requires pdfplumber and accepts `--pdf` explicitly. Its exports are additive and deterministic.

Use the printed local URL for the website; `/api/health` is the new website API health check. Local development bypasses Sites login for public educational content only. It must not host real personal progress. Production requires the Sites identity boundary.

Legacy API diagnostic only:

```powershell
& './constitution_atlas_fullstack/constitution_atlas_fullstack/backend/venv/Scripts/python.exe' -m uvicorn main:app --app-dir './constitution_atlas_fullstack/constitution_atlas_fullstack/backend' --host 127.0.0.1 --port 8000
Invoke-RestMethod http://127.0.0.1:8000/api/health
```

Legacy root `/` is not a frontend; it has no handler. Do not expose that API on the internet.
