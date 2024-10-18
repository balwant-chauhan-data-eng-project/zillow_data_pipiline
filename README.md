# Zillow Data Pipeline 🏡

![Zillow Data Pipeline Project](https://github.com/balwant-chauhan-data-eng-project/zillow_data_pipiline/assets/167126710/bfcbfdef-3222-4892-bc11-c56926c63798)

![Screenshot 1](https://github.com/user-attachments/assets/d15d7d32-1627-49d8-9530-395b7d3cbd2a)
![Screenshot 2](https://github.com/user-attachments/assets/d03142af-7cb9-40e2-9bf7-d4715705cdf7)

---

## Step-by-Step Guide to Set Up Your Zillow Data Pipeline 🛠️

### Step 1: Set Up Your Environment 🌐
1. **Update your system**:
    ```bash
    sudo apt update
    ```

2. **Install necessary packages**:
    ```bash
    sudo apt install python3-pip
    sudo apt install python3.10-venv
    ```

3. **Create a virtual environment**:
    ```bash
    python3 -m venv endtoendyoutube_venv
    ```

4. **Activate the virtual environment**:
    ```bash
    source endtoendyoutube_venv/bin/activate
    ```

5. **Install AWS CLI**:
    ```bash
    pip install --upgrade awscli
    ```

6. **Install Apache Airflow**:
    ```bash
    sudo pip install apache-airflow
    airflow standalone
    ```

7. **Install Amazon provider for Airflow**:
    ```bash
    pip install apache-airflow-providers-amazon
    ```

---

### Step 2: Connect VSCode with EC2 and Create DAG 🖥️
1. **Connect to your EC2 instance using VSCode**.
2. **Create a file inside the Airflow directory**:
   - Name the file `dags.py`.
3. **Write the code for `zilowanalytics.py`**:
   - Define the tasks you will create.

#### Task 1: Extract Zillow Data 📊
- **Function**: `extract_zillow_data_var`
- **Description**: Import dummy data from `zillow_data.py`, create a `raw_data` folder, and dump the raw data into that folder.

#### Task 2: Upload Data to S3 ☁️
- **Function**: `upload_to_s3`
- **Description**: Dump data from the EC2 local file to the `s3_raw_data` bucket.

---

### Step 3: Set Up AWS Lambda for S3 Triggers 🧙‍♂️
1. **Create a Lambda function**.
2. **Create a trigger**:  
   - Set it to activate on `put object` events in the `s3_raw_data` bucket.
3. **Implement the Lambda function**:
   - Write the script for `s3_to_s3` in the Lambda function to dump data into the `s3_staging_data` bucket.

---

### Step 4: Transform Data with Another Lambda Function 🔄
1. **Create another Lambda function**.
2. **Create a trigger**:  
   - Set it to activate on `put object` events in the `s3_staging_data` bucket.
3. **Implement the Lambda function**:
   - Paste the code from `lambda_transform.py` in the Lambda function to dump data into the `s3_transformed_data` bucket.

---

By following these steps, you will successfully set up a data pipeline that extracts, processes, and transforms Zillow data using AWS services! 🎉




step 5: crated a airflow task transfer_s3_to_redshift which will dump data to redhift 



step 6 connect the redshift database with quiksight and visualize it 
