<!-- Assets are self-hosted via tools/make_assets.py -->
<div align="center">
  <img src="assets/banner.svg" alt="Himanshu Upadhyay - Automotive Data Engineer" width="100%">
</div>

<br>

<div align="center">

[![LinkedIn](https://img.shields.io/badge/LinkedIn-hup2000-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/hup2000)
[![Email](https://img.shields.io/badge/Email-himan.upde%40gmail.com-2ea44f?style=flat&logo=gmail)](mailto:himan.upde@gmail.com)
[![Location](https://img.shields.io/badge/Location-Noida%20%2F%20NCR%2C%20India-blue?style=flat&logo=googlemaps)](https://maps.google.com)
[![Status](https://img.shields.io/badge/Open%20To-Azure%20Data%20Engineer%20Roles-brightgreen?style=flat)](#get-in-touch)

</div>

<br>

**Automotive Data Engineer** specializing in converting high-frequency simulation traces, vehicle IoT telemetry, and supply-chain records into clean, idempotent, analytics-grade lakehouse tables.

---

## 🛠️ Engineering Principles

* **Quarantine over dropping:** Invalid records are captured into dead-letter tables with explicit error metadata for lineage tracing.
* **Idempotence by default:** Pipelines allow deterministic re-runs without duplicate side effects or orphaned records.
* **Deterministic ground-truth testing:** Pipeline outputs are validated against independent standalone computation models before merging.
* **Strict schema governance:** Enforced contracts at the ingestion boundary before promotion to Gold/Marts.

---

## 🏗️ Architecture Pattern

```mermaid
flowchart LR
    A["Raw Ingestion<br/>(Telemetry, CAN, MIS)"] --> B["Bronze Layer<br/>(Raw Append + Lineage)"]
    B --> C{"Validation Engine<br/>(Schema & Quality)"}
    C -->|Valid| D["Silver Layer<br/>(Cleaned, Deduplicated)"]
    C -->|Corrupt| Q["Quarantine / DLQ<br/>(Logged Violation)"]
    D --> E["Gold Layer<br/>(Star Schema Marts)"]
    E --> F["Analytics & BI<br/>(SQL Marts, Power BI)"]
```

---

## 🚀 Featured Lakehouse Projects

### 1. [Automotive Simulation Data Lakehouse](https://github.com/himanshuupadhyay300/automotive-simulation-lakehouse)
> **Stack:** PySpark · Spark SQL · Delta Lake · Signal Processing · pytest
* Engineered an automated lakehouse ingesting high-frequency Simulink/CAN vehicle simulation exports.
* Converted raw dynamic signals into discrete threshold-event telemetry (overheating, undervoltage, harsh deceleration).
* **Ground Truth Parity:** Benchmarked Spark transformation against an independent Python engine with 100% agreement (22/22 events validated).
* Built auto-healing pipelines where re-exporting repaired telemetry seamlessly reconciles historical Gold layers.

### 2. [Automotive MIS & KPI Analytics](https://github.com/himanshuupadhyay300/Automotive-MIS-KPI-Analytics-PySpark-SQL-Azure)
> **Stack:** Azure Data Factory · Delta Lake · Star Schema · Dimensional Modeling
* Designed a multi-tier dimensional lakehouse pipeline modeling retail sales, dealer targets, and tractor inventory movements.
* Configured automated late-arriving dimension handling, reconciliation checks, and duplicate deduplication.
* Built 4 business-critical SQL marts (dealer target attainment, inventory turnover, ABC classification, monthly trends) matching finance accounting baselines.

### 3. [IoT Vehicle Telemetry Pipeline](https://github.com/himanshuupadhyay300/iot-vehicle-telemetry-pipeline)
> **Stack:** Medallion Architecture · Azure Databricks · ADLS Gen2 · Event Hubs
* Built an end-to-end streaming/batch vehicle telemetry pipeline with Medallion architecture.
* Implemented schema drift detection, corrupted payload isolation, and idempotent upserts to Delta Lake.
* Includes automated data health scoring and alerting templates for missing sensor heartbeats.

---

## 🧰 Technology & Ecosystem

<div align="center">
  <img src="assets/stack.svg" alt="Himanshu Upadhyay Tech Stack" width="100%">
</div>

| Layer | Technologies |
|---|---|
| **Core Languages** | Python, PySpark, Spark SQL, SQL, MATLAB / Simulink |
| **Azure Lakehouse** | Azure Databricks, Delta Lake, ADLS Gen2, Azure Data Factory |
| **Data Architecture** | Medallion Architecture, Star Schema, Ingestion DLQ, SCD Type 1/2 |
| **Reliability & DevOps**| pytest, CI/CD (GitHub Actions), Git, Schema Enforcement |

---

## 📈 Roadmap & Continuous Improvement

- [x] Simulation signal validation and event boundary generation
- [x] Dimensional modeling & inventory reconciliation framework
- [ ] Production Delta Lake integration on cloud Databricks workspace
- [ ] End-to-end Power BI KPI dashboard layer for MIS data marts
- [ ] Automated SCD Type 2 dimension historical tracking

---

## 📬 Get in Touch

<a href="https://www.linkedin.com/in/hup2000"><img src="assets/btn-linkedin.svg" alt="LinkedIn" height="40"></a>
&nbsp;
<a href="mailto:himan.upde@gmail.com"><img src="assets/btn-email.svg" alt="Email" height="40"></a>

*Open to Data Engineer and Azure Lakehouse roles across Noida, Greater Noida, and Remote.*
