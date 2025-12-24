from typing import Annotated

from fastapi import Depends

from naagin.models.json import CSVListModel
from naagin.models.json import ResourceFileListModel
from naagin.providers.json import provide_csv_list
from naagin.providers.json import provide_resource_list
from naagin.providers.json import provide_resource_list_encrypt

ResourceListDependency = Annotated[ResourceFileListModel, Depends(provide_resource_list)]
ResourceListEncryptDependency = Annotated[ResourceFileListModel, Depends(provide_resource_list_encrypt)]
CSVListDependency = Annotated[CSVListModel, Depends(provide_csv_list)]
