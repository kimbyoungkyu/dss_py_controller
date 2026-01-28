# DSS Python Controller Framework

Python-based Controller Framework for **DSS (Divine Sim Suite)**

이 저장소는 DSS 시뮬레이터와 연동되는 **컨트롤러 SDK**로,
센서 입력(NATS) → 판단 → 제어 출력(UDP) 구조를 표준화합니다.

특히 **카메라 이미지 기반 컨트롤러**를 1급 시민(first-class)으로 설계했습니다.

---

## ✨ 주요 특징

- ✅ **Sensor Input**: NATS + Protobuf  
  - Odom / IMU / Camera(RGB)
- ✅ **Control Output**: UDP (기본 포트 `8886`)
- ✅ **Camera-first State Design**
- ✅ Controller / Sensor / Runtime 완전 분리
- ✅ Rule / RL / MPC / LLM(AgentX) 확장 가능
- ✅ DSS / CarMaker / esmini 구조 공용 가능

---

## 📐 아키텍처 개요

```
[DSS Simulator]
   │
   │  NATS (Protobuf)
   │  - dss.odom
   │  - dss.sensor.imu
   │  - dss.sensor.camera.rgb
   ▼
SensorAdapter
   │
   │  DSSState
   │   ├─ vehicle
   │   ├─ imu
   │   └─ camera (image bytes)
   ▼
Controller (Rule / RL / MPC / AgentX)
   │
   │  DssSetControl (Protobuf)
   ▼
UDPControlPublisher ──► DSS (UDP : 8886)
```

---

## 📁 디렉토리 구조

```
dss_py_controller/
│
├─ proto/
│   ├─ dss_pb2.py
│   └─ README.md
│
├─ core/
│   ├─ state.py
│   ├─ control.py
│   └─ controller_base.py
│
├─ sensors/
│   ├─ sensor_adapter.py
│   └─ fake_sensor.py
│
├─ runtime/
│   ├─ controller_runtime.py
│   └─ udp_control_pub.py
│
├─ controllers/
│   └─ rule_controller.py
│
├─ run_controller.py
├─ requirements.txt
└─ README.md
```

---

## 🔧 설치

```bash
pip install -r requirements.txt
```

---

## ▶ 실행 방법

### Fake Sensor 모드

```bash
python run_controller.py --fake
```

### DSS 연동

```bash
nats-server
python run_controller.py
```

---

## 📸 Camera 사용

```python
if state.camera:
    img_bytes = state.camera.data
    encoding = state.camera.encoding
```

---

## 📄 라이선스

TBD (MIT 권장)
