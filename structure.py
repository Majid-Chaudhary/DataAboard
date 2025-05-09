import os

# Define folders and their files
structure = {
    "auth": ["ldap_auth.py", "jwt_utils.py", "dependencies.py"],
    "api": ["routes_users.py", "routes_workspace.py", "routes_access.py", "__init__.py"],
    "services": ["trino_catalog.py", "gitlab_pipeline.py", "minio_access.py", "openmetadata.py"],
    "models": ["user.py", "workspace.py", "access.py"],
    "utils": ["k8s_provisioner.py", "logger.py", "constants.py"],
}

# Top-level files
top_level_files = [
    "main.py",
    "config.py",
    "requirements.txt",
    ".env"
]

# Create folders and files
for folder, files in structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        path = os.path.join(folder, file)
        with open(path, "w") as f:
            f.write(f"# {file}")

# Create top-level files
for file in top_level_files:
    with open(file, "w") as f:
        f.write(f"# {file}")

print("OpenPlane backend structure created.")
