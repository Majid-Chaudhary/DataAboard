# 🧭 OpenDataPlane (Working Title)

**Self-Service, On-Prem Data Mesh Platform for SQL and ML Workspaces**
Empowering analysts, engineers, and scientists to securely explore and model data — without IT tickets, data exports, or vendor lock-in.

---

## 🚀 Vision

Enable organizations to:

* Discover, request, and access datasets via a unified portal
* Launch isolated, governed SQL and ML workspaces (Trino & Jupyter)
* Enforce table-level access via Trino — not storage hacks
* Run entirely on-prem (MinIO, Ceph, HDFS, LDAP, Kubernetes)
* Stay open-source, auditable, and extensible

---

## 🔍 Problem

Most organizations still rely on central IT for access provisioning, analytics infrastructure, and ML compute.
This creates delays, bottlenecks, and discourages exploration — especially in regulated or on-prem environments.

Existing tools:

* Are cloud-first or vendor-locked (Snowflake, Databricks)
* Don't connect discovery, access control, and compute in one OSS stack
* Assume centralized ETL ownership — which doesn't reflect real orgs

**OpenDataPlane solves this by acting as a control plane above your data — not inside it.**

---

## ⚙️ Architecture Overview (High-Level)

| Component               | Purpose                                                        |
| ----------------------- | -------------------------------------------------------------- |
| **FastAPI**             | Backend API for auth, provisioning, orchestration              |
| **JWT + LDAP**          | Secure authentication + group-based access logic               |
| **Trino**               | Distributed SQL query engine with catalog-based access control |
| **JupyterHub**          | Optional ML workspace per user/team, integrated with Trino     |
| **GitLab CI/CD**        | Automates workspace provisioning & config updates              |
| **Kubernetes**          | Deploys and isolates all compute pods                          |
| **MinIO / Ceph / HDFS** | Storage backend for Iceberg/Delta tables                       |
| **OpenMetadata**        | Data discovery, metadata catalog, and lineage API              |

---

## 🔑 Key Features

* 🌐 Web-based UI for search, access requests, workspace launching
* 🔐 Secure access via LDAP, JWT, and Trino policies
* 📦 S3-compatible or HDFS-based Parquet table access via Trino
* 📊 Jupyter notebooks for ML — directly on Iceberg/Delta data
* 🔎 Metadata and lineage integration via OpenMetadata API
* ⚙️ Fully Kubernetes-native and GitOps-friendly

---

## 🧠 Who Is This For?

* Enterprises with large on-prem datasets and internal analysts
* Data platforms seeking governance without vendor lock-in
* Data science teams who want on-demand compute without fighting IT
* Architects who want composable, OSS-based data control planes

---

## 📅 Project Status

| Feature                   | Status         |
| ------------------------- | -------------- |
| FastAPI backend scaffold  | 🔄 In Progress |
| JWT + LDAP integration    | 🔄 In Progress |
| Trino catalog control     | 🟢 Designed    |
| JupyterHub setup          | 🟢 Designed    |
| GitLab-based workspace CI | 🟢 Designed    |
| OpenMetadata integration  | 🟢 Designed    |

---

## 🧩 Contribute or Follow

This project is actively being developed in the open. We welcome:

* Contributions (code, docs, testing)
* Feedback from enterprise architects or data engineers
* Use case submissions
* Partnerships or early pilots

> GitHub Issues will track feature development and milestones.
> Community docs, deployment recipes, and demo videos coming soon.

---

## 📬 Contact & Updates

Reach out via GitHub, discussions, or contributor Discord (coming soon).
This README will evolve as the first modules are released.

---

> OpenDataPlane is an open-source initiative to bring governed, self-service compute to the heart of on-prem data platforms — without reinventing your storage or pipelines.
