from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class DatabaseSettings(BaseSettings):
    url: str = ...
    
    model_config = SettingsConfigDict(env_prefix='db_', env_file='.env')

class DjangoSettings(BaseSettings):
    secret_key: str = ...
    debug: bool = ...
    allowed_hosts: str = ...
    csrf_trusted_origins: str = ...
    
    @property
    def csrf_trusted_origins_list(self):
        return [origin for origin in self.csrf_trusted_origins.split(",")]
    
    @property
    def allowed_hosts_list(self):
        return [allowed_host for allowed_host in self.allowed_hosts.split(",")]

    model_config = SettingsConfigDict(env_prefix='django_', env_file='.env')

class BotSettings(BaseSettings):
    token: str = ...
    name: str = ...
    admins: str = ...
    web_app_url: str = ...

    model_config = SettingsConfigDict(env_prefix='bot_', env_file='.env')

    @property
    def bot_admins(self):
        self.admins = [int(admin) for admin in self.admins.split(",")]
        return self.admins