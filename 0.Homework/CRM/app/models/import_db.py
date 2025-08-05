from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
import sys
import os

# ../../ 상위 경로(CRM 디렉토리)를 sys.path에 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import config


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

Base = declarative_base()


