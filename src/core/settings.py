from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", case_sensitive=True, extra="ignore")

    APP_DEBUG: bool

    DATABASE_URL: str

    @field_validator("*", mode="before")
    @classmethod
    def strip_quote(cls, v: str) -> str:
        if (
            isinstance(v, str)
            and len(v) > 2
            and (v.startswith("'") and v.endswith("'"))
            or (v.startswith('"') and v.endswith('"'))
        ):
            return v[1:-1]
        return v


settings = Settings.model_validate({})
