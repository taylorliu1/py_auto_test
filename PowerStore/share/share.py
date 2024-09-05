import abc
class ShareBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_nas_server(self,ips,db):
        pass

    @abc.abstractmethod
    def get_trident_client(self,db):
        pass

    @abc.abstractmethod
    def delete_nas_server(self,db):
        pass

    @abc.abstractmethod
    def create_file_interface(self,db):
        pass

    @abc.abstractmethod
    def create_smb_server(self,db):
        pass

    @abc.abstractmethod
    def create_nfs_server(self,db):
        pass

    @abc.abstractmethod
    def create_nfs_export(self,db):
        pass

    @abc.abstractmethod
    def create_smb_share(self,db):
        pass

    @abc.abstractmethod
    def create_file_system(self,fsnum,db):
        pass

    @abc.abstractmethod
    def delete_file_system(self,db):
        pass

    @abc.abstractmethod
    def mount_share(self,db):
        pass

    @abc.abstractmethod
    def ummount_share(self,db):
        pass

