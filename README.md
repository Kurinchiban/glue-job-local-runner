# glue-job-local-runner


# Run AWS Glue Spark Job Locally using Docker

This guide helps you run AWS Glue Spark jobs locally using Docker. Ensure that Docker is installed and running on your system.

---

## Step 1: Pull the Glue Docker Image

Replace `4.0.0` with your desired Glue version.

```bash
docker pull amazon/aws-glue-libs:glue_libs_4.0.0_image_01
```

---

## Step 2: Run Glue ETL Job in Docker

Mount your working directory to the container and start an interactive session.

```bash
docker run --rm -it \
  -v "$PWD:/home/glue" \
  -e AWS_REGION=us-east-1 \
  -e JOB_NAME=my_local_job \
  amazon/aws-glue-libs:glue_libs_3.0.0_image_01 \
  spark-submit /home/glue/script.py --JOB_NAME my_local_job 
```

After running this command, you’ll be inside the Glue Docker container. From here, you can execute your Glue scripts using the Spark context provided in the container.