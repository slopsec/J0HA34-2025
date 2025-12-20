;; This is an operating system configuration generated
;; by the graphical installer.
;;
;; Once installation is complete, you can learn and modify
;; this file to tweak the system configuration, and pass it
;; to the 'guix system reconfigure' command to effect your
;; changes.

;; Indicate which modules to import to access the variables
;; used in this configuration.
(use-modules (gnu) (gnu services) (gnu packages)
             (nongnu packages linux) ;; None-free.
             (nongnu system linux-initrd)) ;; None-free.
(use-service-modules cups desktop networking ssh xorg)


(operating-system
  (kernel linux)
  (initrd microcode-initrd)
  (firmware (list linux-firmware))
  (locale "en_GB.utf8")
  (timezone "Europe/London")
  (keyboard-layout (keyboard-layout "gb"))
  (host-name "Guix")

  ;; The list of user accounts ('root' is implicit).
  (users (cons* (user-account
                  (name "saorsa")
                  (comment "Dylan")
                  (group "users")
                  (home-directory "/home/saorsa")
                  (supplementary-groups '("wheel" "netdev" "audio" "video")))
                %base-user-accounts))

  ;; Packages installed system-wide.  Users can also install packages
  ;; under their own account: use 'guix search KEYWORD' to search
  ;; for packages and 'guix install PACKAGE' to install a package.
  (packages (append (list librewolf) %base-packages))

  ;; Below is the list of system services.  To search for available
  ;; services, run 'guix system search KEYWORD' in a terminal.
  (services
    (append
      (list (service plasma-desktop-service-type)
            (service openssh-service-type)
            (service tor-service-type)
            (service cups-service-type)
            (set-xorg-configuration
              (xorg-configuration (keyboard-layout keyboard-layout))))
      (modify-services %desktop-services
        (guix-service-type config =>
          (guix-configuration
            (inherit config)
            (substitute-urls
              (cons "https://substitutes.nonguix.org"
                    %default-substitute-urls))
            (authorized-keys
              (cons (local-file "./signing-key.pub")
                    %default-authorized-guix-keys)))))))


  ;; The list of file systems that get "mounted".  The unique
  ;; file system identifiers there ("UUIDs") can be obtained
  ;; by running 'blkid' in a terminal.

  (define btrfs-options
    '("noatime" "space_cache=v2" "compress=zstd" "ssd" "discard=async"))

  (file-systems
    (cons*
      (file-system
        (mount-point "/")
        (device (uuid "UUID" 'btrfs))
        (type "btrfs")
        (options (cons "subvol=@" btrfs-options)))
      (file-system
        (mount-point "/home")
        (device (uuid "UUID" 'btrfs))
        (type "btrfs")
        (options (cons "subvol=@home" btrfs-options)))
      (file-system
        (mount-point "/guix")
        (device (uuid "UUID" 'btrfs))
        (type "btrfs")
        (options (cons "subvol=@guix" btrfs-options)))
      (file-system
        (mount-point "/var")
        (device (uuid "UUID" 'btrfs))
        (type "btrfs")
        (options (cons "subvol=@var" btrfs-options)))
      ;; Repeat for /guix and /var
      (file-system
        (mount-point "/boot/efi")
        (device (uuid "EFIID" 'fat32))
        (type "vfat"))
      %base-file-systems))

