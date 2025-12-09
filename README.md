# Building Scalable AI with Ray - Virtual Hands-On Lab

This repository contains materials for the **Live Virtual Hands-On Lab: Building Scalable AI with Ray**, where ML engineers and platform engineers explore how to use Ray for distributed data processing, model training, and real-time inference with the Anyscale Platform.

## What You'll Learn

In this virtual session, you'll learn how to use Ray to:

- **Ingest data at scale** - Load and process large datasets efficiently across distributed systems
- **Transform data using Ray Data pipelines and operators** - Build scalable data transformation workflows
- **Join Ray Datasets and apply transformations to joined columns** - Combine multiple data sources and process them together
- **Run batch inference on GPUs at scale** - Leverage GPU resources for high-throughput ML inference
- **Integrate LLM inference with fractional resource scheduling** - Optimize resource utilization for large language models

This free lab is more than a webinar. You'll leave with a working understanding of Ray, a reusable project you can build on, and a clear view of how Ray and Anyscale work together to accelerate AI development.

![Ray Overview](assets/img01.png)

## Contents

### Main Lab Notebook: `VHOL.ipynb`

The main hands-on lab notebook (`VHOL.ipynb`) guides you through building a complete scalable AI pipeline. You'll work through:

1. **Introduction to Ray** - Learn core Ray concepts including tasks, actors, and the Ray ecosystem

   ![Ray Tasks](assets/img02.png)

2. **Introduction to Ray Data** - Understand streaming execution, blocks, and distributed data processing

   ![Ray Data Blocks](assets/img03.png)

   **Traditional Bulk Processing:**  
   ![Bulk Processing](assets/img04.png)  
   
   **Streaming Execution**: Ray Data processes large datasets efficiently using a streaming model with blocks as the basic units of data, enabling pipeline parallelism and memory-efficient processing.

   ![Streaming Processing](assets/img05.png)  
   - Enables pipeline parallelism, allowing data to flow through multiple processing stages concurrently for increased efficiency.

3. **Building a Scalable AI Pipeline** - Create an end-to-end pipeline that:
   - Ingests image prompts and metadata from CSV files
   - Transforms and enriches prompts using Ray Data operators
   - Joins multiple datasets (animals and clothing details)
   - Generates images at scale using distributed GPU inference
   - Enhances prompts with LLM-based transformations
   - Exports results to storage (Parquet and PNG formats)

**Scenario**: You'll build a pipeline that combines animal prompts with clothing details, enhances them using an LLM, and generates images using a text-to-image model—all orchestrated at scale with Ray Data.

![Pipeline Progress](assets/img06.png)

![Pipeline Progress](assets/Part2.png)

![Pipeline Progress](assets/Part3.png)


**Key Learning Points**:
- Ray Data's streaming execution model for memory-efficient processing
- Actor-based patterns for stateful operations (like model loading)
- Fractional GPU scheduling for optimal resource utilization
- Dataset joins and transformations in distributed settings
- Parameterization and separation of concerns in ML pipelines


### Bonus Code: `code/` Directory

Explore additional examples and advanced patterns beyond the main lab:

#### Core Examples (`code/`)
- **`sequential_process.py`** - Demonstrates sequential processing without Ray
- **`parallel_process.py`** - Shows how to parallelize the same process using Ray Tasks
- **`ray_actor_counter.py`** - Example of using Ray Actors for stateful distributed operations

#### Bonus Modules (`code/bonus/`)

##### 1. Batch Inference Optimization (`code/bonus/batch-inference-optimization/`)
**Time**: ~65 minutes | **Difficulty**: Intermediate

Learn production-grade ML inference optimization patterns:
- **Part 1: Inference Fundamentals** - Compare inefficient vs. efficient inference approaches, understand actor-based patterns
- **Part 2: Ray Data Architecture** - Deep dive into streaming execution, memory models, and operator fusion
- **Part 3: Advanced Optimization** - Systematic optimization techniques, multi-model ensembles, performance monitoring

**Key Topics**: Model loading optimization, batch sizing strategies, resource management, concurrency tuning, performance monitoring with Ray Dashboard.

##### 2. ETL Processing and Optimization (`code/bonus/etl-optimization/`)
**Time**: ~40 minutes | **Difficulty**: Intermediate

Build comprehensive ETL pipelines using Ray Data:
- **ETL Fundamentals with TPC-H** - Learn using industry-standard TPC-H benchmark data
- **Data Transformations and Processing** - Customer segmentation, order enrichment, filtering, aggregations
- **Performance Optimization Techniques** - Batch sizing, column pruning, memory management
- **Large-Scale ETL Patterns** - Multi-dimensional aggregations, data warehouse integration

**Key Topics**: TPC-H benchmark patterns, distributed joins, filter pushdown, column selection optimization, writing to Snowflake/BigQuery/Parquet.

##### 3. Unstructured Data Ingestion (`code/bonus/unstructured-data-ingestion/`)
**Time**: ~35 minutes | **Difficulty**: Advanced

Build document ingestion pipelines for data lakes:
- **Data Lake Document Discovery** - Locate and catalog unstructured documents
- **Document Processing and Classification** - Process and categorize documents at scale
- **Text Extraction and Enrichment** - Extract and enhance text content
- **Data Warehouse Output** - Transform unstructured data into analytics-ready formats

**Key Topics**: Document processing, text extraction, classification, data lake to data warehouse workflows.
