# DataAboard (Working Title)

## Self-Service, On-Prem Data Mesh / Democratization Platform

Empowering everyone from analysts, engineers, and scientists to ordinary users to securely discover, access, and model data – without IT tickets, data exports, or vendor lock-in.

---

## Vision

In today's data-driven world, organizations are bottlenecked by centralized data access and compute provisioning, especially in on-premise or highly regulated environments. DataAboard's vision is to enable organizations to:

* **Discover, request, and access datasets via a unified portal**, making data easily findable and understandable.
* **Launch isolated, governed SQL and ML workspaces** on-demand, accelerating time to insight.
* **Enforce granular, table-level access policies** by design, ensuring security and compliance without complex storage hacks.
* **Run entirely on-premise**, leveraging existing infrastructure and ensuring data sovereignty.
* **Stay open-source, auditable, and extensible**, fostering community and avoiding vendor lock-in.

We believe data democratization shouldn't compromise governance or security, especially when data cannot leave your premises.

## The Problem DataAboard Solves

Most organizations still rely on central IT for access provisioning, analytics infrastructure, and ML compute. This creates:

* **Delays and Bottlenecks:** Lengthy IT ticket processes for data access and environment setup.
* **Limited Exploration:** Discouragement of ad-hoc analysis due to friction.
* **Lack of Control:** Over-reliance on vendor-specific tools that are often cloud-first, leading to vendor lock-in and data residency challenges.
* **Governance Gaps:** Difficulty implementing consistent, auditable access control across diverse on-prem data sources.

**DataAboard solves this by acting as a pragmatic, open-source control plane over your existing data infrastructure.** We don't reinvent the wheel; we connect the best wheels together to deliver a seamless experience.

## The DataAboard Philosophy: "Connectors + Simplicity + No Headache"

Inspired by projects like Airbyte, DataAboard focuses on abstracting complexity through existing community "connectors" and a streamlined user experience:

* **No Reinventing Core Engines:** We don't build new query engines, object storage systems, or metadata platforms. Instead, we integrate and orchestrate battle-tested open-source components.
* **Connectors to Infrastructure:** DataAboard doesn't build its own connectors. Instead, it reuses existing, community-tested connectors from platforms like OpenMetadata and Trino. OpenMetadata acts as the single source of truth for discovery and lineage, while Trino handles querying across sources via its rich connector ecosystem. This ensures maximum compatibility, minimal maintenance, and full reuse of trusted components — no reinvention required.
* **Simplicity for Users:** Through a unified portal and intuitive GitOps-based access requests, users can focus on *what data they need* and *what analysis they want to perform*, not *how to get access* or *how to provision compute*.
* **No Operational Headaches:** Automated provisioning, consistent governance enforcement, and leveraging resilient open-source tools reduce manual operational burdens for platform teams.

## Architecture Overview (High-Level)

<p align="center">
  <img src="./assets/DataAboard.jpg"
       alt="Federated Data Access"
       width="700"
       style="border: 1px solid #ccc; border-radius: 6px; padding: 6px;" />
  <br/>
  <em>MVP-Figure: GitOps-based access control using Iceberg, Trino, and Kubernetes</em>
  <br/>
  <em>Support for further integrations will be added later by adding community connectors</em>
</p>

DataAboard provides an intelligent orchestration layer using a set of well-established open-source components:

* **FastAPI Backend:** The core API for authentication, user provisioning, and orchestrating data and compute resources.
* **JWT + LDAP:** Secure authentication and group-based access logic, integrating with existing enterprise identity providers.
* **Kubernetes:** The foundational platform for deploying and isolating all compute pods (Trino, JupyterHub, etc.) ensuring scalability and resource governance.
* **OpenMetadata (Metadata Source of Truth):**

  * **Purpose:** The central hub for all data discovery, metadata cataloging, and lineage tracking.
  * **Strategy:** DataAboard makes **live API calls to OpenMetadata** to gather real-time metadata (schemas, descriptions, lineage) from various sources. We do not ingest or duplicate the metadata within DataAboard, ensuring OpenMetadata remains the definitive source of truth.
* **Trino (Universal Query Engine):**

  * **Purpose:** A high-performance distributed SQL query engine for federated querying across diverse data sources.
  * **Strategy:** DataAboard configures and manages Trino, which uses its own rich set of connectors to query underlying data. This enables users to perform **single, federated queries across Data Warehouses (DWH), Data Lakehouses (DLH - Iceberg, Delta, Hudi), and traditional Hive** installations, abstracting away underlying data complexities. Trino also serves as the primary enforcement point for granular, table-level access policies.
* **JupyterHub (Optional ML Workspace):** Provides isolated, customizable ML workspaces per user or team, deeply integrated with Trino for direct access to governed data.
* **GitLab CI/CD:** Automates workspace provisioning, configuration updates, and crucially, **processes user data access requests via Git branch creation**, ensuring an auditable and version-controlled governance flow.
* **MinIO / Ceph / HDFS:** Flexible storage backends for your open table formats (Iceberg, Delta) on-premise, ensuring data sovereignty.

## Key Features

* **Web-based UI:** Intuitive portal for data search, access requests, and workspace launching.
* **Secure & Granular Access:** Robust security via LDAP, JWT, and Trino policies, with GitOps-driven access provisioning ensuring traceability.
* **Federated Data Querying:** Access S3-compatible, HDFS-based, or traditional database tables via Trino's powerful federated query capabilities.
* **Integrated ML Workspaces:** Jupyter notebooks for ML directly on governed Iceberg/Delta data.
* **Metadata & Lineage:** Seamless integration with OpenMetadata for comprehensive data discovery and understanding.
* **Kubernetes-Native & GitOps-Friendly:** Fully automated deployment and management of compute and storage on Kubernetes, supporting modern GitOps workflows.
* **On-Premise Focus:** Designed from the ground up for enterprise data sovereignty and security requirements.

## Federated Data Ownership & Access Control (Design Principles)

* **Domain Ownership:** Each department owns its own MiniIO (S3) bucket (or other compatible storage) containing its fact tables.
* **Open Table Formats:** Tables are stored in **Apache Iceberg** format (with plans for Delta Lake and Apache Hudi connectors), ensuring schema evolution, versioning, and ACID properties.
* **Shared Dimensions:** Dimension tables are globally readable across departments for consistent analytics.
* **GitOps for Access:** Users request data access by creating a GitLab branch. A CI/CD pipeline automates the provisioning of **scoped read-only access via Trino**, limited to the requested fact tables.
* **Traceability:** This ensures data product-level security, domain autonomy, and full traceability of all access grants.

## Self-Service Compute & Analytics Workspace (User Experience)

* **On-Demand Provisioning:** DataAboard's CI/CD pipeline provisions a dedicated SQL (Trino) and/or ML (JupyterHub) workspace for each user or team.
* **Empowered Users:** Within their isolated compute environment, users can:

  * Run ad hoc SQL queries on Trino across any accessible data source.
  * Create dashboards, reports, or aggregated cubes.
  * Export results into Parquet format for reuse or sharing as new data products.
* **Isolation & Scalability:** All compute is isolated per user/team and dynamically scalable via Kubernetes, preventing resource conflicts and ensuring consistent performance.
* **Core Philosophy:** This promotes collaborative analysis, domain independence, and the "data-as-a-product" philosophy by providing immediate, governed access to compute alongside data.

## Future Vision: LLM Integration (v2)

While the MVP focuses on building a robust data mesh foundation, our **v2 roadmap** includes deep integration with Large Language Models (LLMs):

* **Secure On-Prem LLM Training:** DataAboard's governed, on-premise data products will provide the ideal, secure, and compliant source for training and fine-tuning private, company-specific LLMs.
* **AI-Powered Data Discovery:** Leveraging OpenMetadata's rich metadata, LLMs will enable natural language querying of the data catalog, allowing users to find and understand data simply by asking questions.
* **Enhanced Data Workflows:** LLMs can assist in automating data quality checks, suggesting data transformation logic, and generating documentation, further simplifying data operations.
* **Self-Service AI Applications:** The JupyterHub workspaces will evolve to support the development and deployment of internal AI applications that leverage the governed data.

By building a strong data foundation first, DataAboard ensures that your future LLM initiatives will operate on reliable, secure, and well-understood data.

## Project Status

This project is actively being developed in the open, targeting a **robust MVP launch within approximately one year**.

* FastAPI backend scaffold: **In Progress**
* JWT + LDAP integration: **In Progress**
* Trino catalog control: **Designed** (Implementation starting soon)
* JupyterHub setup: **Designed** (Implementation starting soon)
* GitLab-based workspace CI/CD: **Designed** (Implementation starting soon)
* OpenMetadata integration: **Designed** (Implementation starting soon)
* Core Kubernetes deployments: **In Progress**
* Initial documentation & deployment recipes: **Starting Soon**

We are prioritizing core functionality to deliver a stable and valuable initial release.

## Contribute or Follow

This project is open-source and thrives on community involvement. We welcome:

* **Contributions:** Code, documentation, testing, and bug reports.
* **Feedback:** From enterprise architects, data engineers, and data scientists on use cases and features.
* **Partnerships or Early Pilots:** We are looking for organizations interested in piloting DataAboard in their on-prem environments.

Follow our progress via GitHub Issues for feature development and milestones. Community discussions, detailed deployment recipes, and demo videos are coming soon.

## Contact & Updates

Reach out via GitHub discussions, or join our contributor Discord (coming soon). This `README.md` will continue to evolve as the first modules are released and the project matures.

---