from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://user:password@postgresserver/db"

    SECRET_KEY: str = "5e7f8754073e5e9dd4eed3b3f1d797673670aa3eda75448ba0eb826fe738bef1"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        from_attributes = True


settings = Settings()
