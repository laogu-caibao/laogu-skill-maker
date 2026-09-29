import zipfile, os, re, sys

D = os.path.expanduser("~/workspace/skills/dist")
fails = []
passes = 0
for fn in sorted(os.listdir(D)):
    if not fn.endswith(".zip"):
        continue
    slug = fn.rsplit("-", 2)[0]  # laogu-fundamentals from laogu-fundamentals-1.0.1.zip
    path = os.path.join(D, fn)
    issues = []
    try:
        z = zipfile.ZipFile(path)
        names = z.namelist()
        # 1. SKILL.md at root
        if "SKILL.md" not in names:
            issues.append("SKILL.md not at zip root")
        else:
            # 2. frontmatter name+description
            head = z.read("SKILL.md").decode("utf-8", "replace")[:2000]
            m = re.match(r"^---\s*\n(.*?)\n---\s*\n", head, re.S)
            if not m:
                issues.append("no YAML frontmatter")
            else:
                fm = m.group(1)
                nm = re.search(r"^name:\s*[\"']?(.+?)[\"']?\s*$", fm, re.M)
                ds = re.search(r"^description:\s*[\"']?(.+?)[\"']?\s*$", fm, re.M)
                if not nm or not nm.group(1).strip():
                    issues.append("frontmatter name missing")
                if not ds or not ds.group(1).strip():
                    issues.append("frontmatter description missing")
        # 3. references/ not flattened
        if not any(n.startswith("references/") for n in names):
            issues.append("references/ missing or flattened")
    except Exception as e:
        issues.append(f"zip error: {e}")
    if issues:
        fails.append((slug, issues))
    else:
        passes += 1
    # 4. slug consistency: zip name slug vs frontmatter name (normalize _ to -)
print(f"PASS: {passes}/16")
for slug, issues in fails:
    print(f"FAIL {slug}: {issues}")
