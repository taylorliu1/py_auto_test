import abc
class ShareBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_trident_client(self,db):
        pass

    @abc.abstractmethod
    def connect_host_Dynamic_discover(self,ips,db):
        pass

    @abc.abstractmethod
    def delete_connect_host_Dynamic_discover(self,db):
        pass

    @abc.abstractmethod
    def array_computer_add(self,db):
        pass

    @abc.abstractmethod
    def delete_array_computer_add(self,db):
        pass


    @abc.abstractmethod
    def create_file_system(self,fsnum,db):
        pass


    @abc.abstractmethod
    def create_volume(self,db):
        pass

    @abc.abstractmethod
    def delete_create_volume(self,db):
        pass

