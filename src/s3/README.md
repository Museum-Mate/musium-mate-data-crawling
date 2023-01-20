## **사용방법** 

<br>

- 사용 방법은 크게 4가지가 있습니다.
- ① 다운로드 파일 : `.download_file(src_path, dest_path)`
    - S3 스토리지에서 파일을 다운로드합니다.
        - src_path : 다운로드할 S3 스토리지의 파일 이름을 포함하는 파일 경로. (버킷 이름 제외)
        - dest_path : 저장할 로컬 경로.
    - 예 : file_example.zip이 local_example에 저장됩니다.
        - src_path : 경로/.../.../s3_storage/file_example.zip
        - 목적지 경로 : C://.../.../local_example

<br>

- ② 다운로드 폴더 : `.download_folder(src_path, dest_path)`
    - S3 스토리지에서 폴더를 다운로드합니다.
        - src_path : 다운로드할 S3 스토리지의 폴더 경로(S3 스토리지의 접두사). (버킷 이름 제외)
        - dest_path : 저장할 로컬 경로.
    - 예시 : s3_storage_example 폴더가 local_example에 저장됩니다.
        - src_path : 경로/.../.../s3_storage_example
        - 목적지 경로 : C://.../.../local_example

<br>

- ③ 업로드 파일 : `.upload_file(src_path, dest_path)`
    - 로컬에서 S3 스토리지로 파일을 업로드합니다.
        - src_path : 업로드할 로컬 파일 경로. (버킷 이름 제외)
        - dest_path : S3 스토리지의 경로
    - 예시 : file_example.zip이 s3_storage_example에 저장됩니다.
        - src_path : C://.../.../local/file_example.zip
        - dest_path : 경로/.../.../s3_storage_example

<br>

- ④ 업로드 폴더 : `.upload_folder(src_path, dest_path)`
    - 로컬에서 S3 스토리지로 폴더를 업로드합니다.
        - src_path : 업로드할 로컬의 폴더 경로. (버킷 이름 제외)
        - dest_path : S3 스토리지의 경로
    - 예시 : local_example 폴더는 s3_storage_example에 저장됩니다.
        - src_path : C://.../.../local_example
        - dest_path : 경로/.../.../s3_storage_example

<br>

- ⑤ check_path_exists : `.check_path_exists(경로)`
    - 입력 경로(디렉토리 또는 파일)가 존재하는지 확인합니다.
        - 경로 : 디렉토리 경로 또는 디렉토리 + 파일 경로
    - 예 : 경로 존재 결과에 따라 True/False를 반환합니다.
        - 예1) 경로 : path/.../.../s3_storage_example
        - 예2) 경로 : 경로/.../.../s3_storage_example/file_example.zip

<br>

## **Example**

<br>

```python
BUCKET_NAME = "USE_REAL_BUCKET_NAME"
ACCESS_KEY = "USE_REAL_ACCESS_KEY"
SECRET_KEY = "USE_REAL_SECRET_KEY"
ENDPOINT_URL = "USE_REAL_ENDPOINT_URL_IF_NECESSARY"

s3_updownloader = S3UpDownLoader(
        bucket_name = BUCKET_NAME,
        access_key = ACCESS_KEY,
        secret_key = SECRET_KEY,
        endpoint_url  = ENDPOINT_URL,
        verbose = False
    )

# ① S3 스토리지에서 로컬로 파일을 다운로드합니다.
src_path="path/.../.../s3_storage/file_example.zip"
dest_path="C://.../.../local_example"
s3_updownloader.download_file(src_path, dest_path)

# ② S3 스토리지에서 로컬로 폴더를 다운로드합니다.
src_path="path/.../.../s3_storage_example"
dest_path="C://.../.../local_example"
s3_updownloader.download_folder(src_path, dest_path)

# ③ 로컬 스토리지에서 S3 스토리지로 파일 업로드
src_path="C://.../.../local/file_example.zip"
dest_path="path/.../.../s3_storage_example"
s3_updownloader.upload_file(src_path, dest_path)

# ④ 로컬 저장소에서 S3 저장소로 폴더 업로드
src_path="C://.../.../local_example"
dest_path="path/.../.../s3_storage_example"
s3_updownloader.upload_folder(src_path, dest_path)

# ⑤ 입력 경로(디렉토리 또는 파일)가 존재하는지 확인합니다.
path1 = "path/.../.../s3_storage_example"
path2 = "path/.../.../s3_storage_example/file_example.zip"

if s3_updownloader.check_path_exists(path1):
    print("s3_storage_example folder exists.")
else:
    print("s3_storage_example folder dosen't exist.")
if s3_updownloader.check_path_exists(path2):
    print("file_example.zip file exists.")
else:
    print("file_example.zip file dosen't exist.")
```

<br>

## **How to use run_updownload.py**

<br>

```python
python3 run_updownload.py \
    --updown=up \                                       # (필수) 업로드하려면 'up'을 입력하고 다운로드하려면 'down'을 입력합니다.
    --filefolder=file \                                 # (필수) 파일의 경우 'file'을, 폴더의 경우 'folder'를 입력합니다.
    --src_path=C://.../.../local/file_example.zip \     # (필수) 업로드/다운로드할 파일 또는 폴더의 경로를 입력합니다.
    --dest_path=path/.../.../s3_storage_example \      # (필수) 업로드/다운로드할 파일 또는 폴더의 경로를 입력합니다.
    --bucket_name=USE_REAL_BUCKET_NAME \                # (선택사항) bucket name.
    --access_key=USE_REAL_ACCESS_KEY \                  # (선택사항) access key.
    --secret_key=USE_REAL_SECRET_KEY \                  # (선택사항) secret key.
    --endpoint_url=USE_REAL_ENDPOINT_URL_IF_NECESSARY \ # (선택사항) endpoint url for S3 Compatible Storage.
    --verbose=False                                   \ # (선택사항) verbose
```

<br>