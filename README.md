# zillow_data_pipiline

![_zillow_data_pipeline_project](https://github.com/balwant-chauhan-data-eng-project/zillow_data_pipiline/assets/167126710/bfcbfdef-3222-4892-bc11-c56926c63798)

![Screenshot 2024-04-15 225940](https://github.com/user-attachments/assets/1b76811b-a253-4e87-8089-95a546c65006)
![Screenshot 2024-04-15 200605](https://github.com/user-attachments/assets/a87df9ba-2f3c-472b-9695-77f580e12cd2)
![Screenshot 2024-04-15 200628](https://github.com/user-attachments/assets/d15d7d32-1627-49d8-9530-395b7d3cbd2a)
![Screenshot 2024-04-15 225940](https://github.com/user-attachments/assets/d03142af-7cb9-40e2-9bf7-d4715705cdf7)


step 1:
sudo apt update
sudo apt install python3-pip
sudo apt install python3.10-venv
python3 -m venv endtoendyoutube_venv
source endtoendyoutube_venv/bin/activate
pip install --upgrade awscli
sudo pip install apache-airflow
airflow standalone
pip install apache-airflow-providers-amazon

step 2:
connect vscode with ec2
create file inside airflow dags.py
write the code of zilowanalytics.py
where we had created the task




task 1: extact_zilow_data_var (importing dummy data from zillow_data.py and creating the raw_data folder and dumping raw data into thath)




task 2 : dumping data from ec2 local file to s3_raw_data  bucket using task upload_to_s3




step 3 : create a lambda and create a trigger (put object) into s3_raw_data and then script of lambda s3_to_s3 code in lambda function which will dump data in s3_staging_data



step 4 : create a lambda and create a trigger (put object) into s3_staging_data and then s3_staging_data paste the code of lambda_trnasform.py which dump data to s3_trasformed_data




step 5: crated a airflow task transfer_s3_to_redshift which will dump data to redhift 



step 6 connect the redshift database with quiksight and visualize it 
