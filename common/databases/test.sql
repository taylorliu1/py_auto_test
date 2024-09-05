CREATE TABLE IF NOT EXISTS `trident_objs` (
    `IP` VARCHAR(100) NOT NULL,
    `USER` VARCHAR(100) NULL,
    `PASSWORD`VARCHAR(40) NULL,
    PRIMARY KEY (`IP`))ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `pflex_objs` (
    `IP` VARCHAR(100) NOT NULL,
    `USER` VARCHAR(100) NULL,
    `PASSWORD`VARCHAR(40) NULL,
    PRIMARY KEY (`IP`))ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `vm_objs` (
    `VM_NAME` VARCHAR(100) NOT NULL,
    `VM_IP` VARCHAR(100) NULL,
    `TYPE` VARCHAR(100) NULL,
    `mount_point` VARCHAR(100) NULL,
    `datastore` VARCHAR(100) NULL,
    PRIMARY KEY (`VM_NAME`))ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `nas_objs` ( 
    `nas_ip` VARCHAR(100) NULL, 
    `nas_id` VARCHAR(100) NOT NULL, 
    `nas_name` VARCHAR(40) NULL, 
    PRIMARY KEY ( `nas_id` ))ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `pflex_nas_objs` ( 
    `nas_ip` VARCHAR(100) NULL, 
    `nas_id` VARCHAR(100) NOT NULL, 
    `nas_name` VARCHAR(40) NULL, 
    `protection_domain_id` VARCHAR(40) NULL,
    PRIMARY KEY ( `nas_id` ))ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `filesystem_objs` (
    `nas_id` VARCHAR(100) NULL,
    `filesystem_name` VARCHAR(100) NOT NULL,
    `filesystem_id` VARCHAR(100) NOT NULL,
    `filesystem_type` VARCHAR(100) NULL,
    `nfspath` VARCHAR(100) NULL,
    `smbpath` VARCHAR(100) NULL,
    PRIMARY KEY ( `filesystem_id` ))ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `datastore_objs` ( 
    `NFS_datastore` VARCHAR(100) NOT NULL, 
    `Esxi_host` VARCHAR(100) NOT NULL,
    `height` INT DEFAULT 0,
    PRIMARY KEY ( `NFS_datastore`,`Esxi_host` ))ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `block_datastore_objs` ( 
    `VMFS_datastore` VARCHAR(100) NOT NULL, 
    `Esxi_host` VARCHAR(100) NOT NULL,
    `height` INT DEFAULT 0,
    PRIMARY KEY ( `VMFS_datastore`,`Esxi_host` ))ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `host_volume_mapping` ( 
    `host` VARCHAR(100) NOT NULL, 
    `volume_name` VARCHAR(100) NULL,
    `volume_wwn` VARCHAR(100) NULL,
    `volume_id` VARCHAR(100) NULL)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `sdc_volume_mapping` ( 
    `host` VARCHAR(100) NOT NULL, 
    `volume_name` VARCHAR(100) NULL,
    `volume_id` VARCHAR(100) NULL,
    `sdc_id` VARCHAR(100) NULL)ENGINE=InnoDB DEFAULT CHARSET=utf8;