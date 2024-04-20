## Backend

### 설치

```
python -m venv/venv
source venv/bin/activate
pip install -r requirements.txt
```

### 실행

```
python main.py
```

### 테스트

```
python -m pytest tests
```

### 커버리지 확인

```
python -m pytest --cov-report term --cov=tests
```

### Pre-commit check

```
pre-commit autoupdate
pre-commit install
pre-commit run --all-files
```
