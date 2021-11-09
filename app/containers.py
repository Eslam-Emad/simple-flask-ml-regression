from dependency_injector import containers, providers

from app import repository


class Container(containers.DeclarativeContainer):
    repository_provider = providers.Factory(repository.Repository)
