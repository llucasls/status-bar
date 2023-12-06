ID != . /etc/os-release; printf '%s' "$${ID}"

ifeq ($(ID),debian)
    INSTALL = apt-get install
    PACKAGES = $(file < requirements_debian.txt)
else ifeq ($(ID),artix)
    INSTALL = pacman -S
    PACKAGES = $(file < requirements_artix.txt)
endif

install:
	$(INSTALL) $(PACKAGES)
