import os

def _criar_arquivo(place):
	open(place).close()

#a
#os.abc
#os.abort
#os.access
#os.altsep

#c
criar_arquivo = _criar_arquivo # criar um arquivo
#os.chmod
#os.chown
#os.chroot
mudar_pasta_atual = os.chdir # cd
fechar_fd = os.close # syscall close
fechar_varios_fds = os.closerange # fechar todos os FDs [fd_low, fd_high[
checar_configuracao_de_compilacao = os.confstr # chechar variável da configuração do sitema
pegar_configuracao_de_compilacao = os.confstr_names # pegar um dicionário com todas configurações do sistema
copiar_bytes_fd = lambda: os.copy_file_range # copiar N bytes de um fd para outro
numero_de_cpus = os.cpu_count # contar o numero de cores da cpu
nome_do_terminal = os.ctermid # pegar o nome do terminal master 
#os.curdir

#g
pasta_atual = os.getcwd # pwd / %cd%
ler_variavel = os.getenv # echo
tamanho_do_terminal = os.get_terminal_size
#l
listar_pasta = os.listdir # ls / dir
#m
criar_pasta = os.mkdir # mkdir
#r
deletar_pasta = os.rmdir # rm -r / del -r
#p
juntar_path = os.path.join # path/do/arquivo / path\do\arquivo
checar_arquivo_existe = os.path.exists # [[ -f arquivo ]] / exists arquivo

#os.defpath
#os.device_encoding
#os.devnull
#os.dup
#os.dup2
#os.environ
#os.environb
#os.error
#os.eventfd
#os.eventfd_read
#os.eventfd_write
#os.execl
#os.execle
#os.execlp
#os.execlpe
#os.execv
#os.execve
#os.execvp
#os.execvpe
#os.extsep
#os.fchdir
#os.fchmod
#os.fchown
#os.fdatasync
#os.fdopen
#os.fork
#os.forkpty
#os.fpathconf
#os.fsdecode
#os.fsencode
#os.fspath
#os.fstat
#os.fstatvfs
#os.fsync
#os.ftruncate
#os.fwalk
#os.get_blocking
#os.get_exec_path
#os.get_inheritable
#os.get_terminal_size
#os.getcwd
#os.getcwdb
#os.getegid
#os.getenv
#os.getenvb
#os.geteuid
#os.getgid
#os.getgrouplist
#os.getgroups
#os.getloadavg
#os.getlogin
#os.getpgid
#os.getpgrp
#os.getpid
#os.getppid
#os.getpriority
#os.getrandom
#os.getresgid
#os.getresuid
#os.getsid
#os.getuid
#os.getxattr
#os.initgroups
#os.isatty
#os.kill
#os.killpg
#os.lchown
#os.linesep
#os.link
#os.listdir
#os.listxattr
#os.lockf
#os.login_tty
#os.lseek
#os.lstat
#os.major
#os.makedev
#os.makedirs
#os.memfd_create
#os.minor
#os.mkdir
#os.mkfifo
#os.mknod
#os.name
#os.nice
#os.open
#os.openpty
#os.pardir
#os.path
#os.pathconf
#os.pathconf_names
#os.pathsep
#os.pidfd_open
#os.pipe
#os.pipe2
#os.popen
#os.posix_fadvise
#os.posix_fallocate
#os.posix_spawn
#os.posix_spawnp
#os.pread
#os.preadv
#os.putenv
#os.pwrite
#os.pwritev
#os.read
#os.readlink
#os.readv
#os.register_at_fork
#os.remove
#os.removedirs
#os.removexattr
#os.rename
#os.renames
#os.replace
#os.rmdir
#os.scandir
#os.sched_get_priority_max
#os.sched_get_priority_min
#os.sched_getaffinity
#os.sched_getparam
#os.sched_getscheduler
#os.sched_param
#os.sched_rr_get_interval
#os.sched_setaffinity
#os.sched_setparam
#os.sched_setscheduler
#os.sched_yield
#os.sendfile
#os.sep
#os.set_blocking
#os.set_inheritable
#os.setegid
#os.seteuid
#os.setgid
#os.setgroups
#os.setpgid
#os.setpgrp
#os.setpriority
#os.setregid
#os.setresgid
#os.setresuid
#os.setreuid
#os.setsid
#os.setuid
#os.setxattr
#os.spawnl
#os.spawnle
#os.spawnlp
#os.spawnlpe
#os.spawnv
#os.spawnve
#os.spawnvp
#os.spawnvpe
#os.splice
#os.st
#os.stat
#os.stat_result
#os.statvfs
#os.statvfs_result
#os.strerror
#os.supports_bytes_environ
#os.supports_dir_fd
#os.supports_effective_ids
#os.supports_fd
#os.supports_follow_symlinks
#os.symlink
#os.sync
#os.sys
#os.sysconf
#os.sysconf_names
#os.system
#os.tcgetpgrp
#os.tcsetpgrp
#os.terminal_size
#os.times
#os.times_result
#os.truncate
#os.ttyname
#os.umask
#os.uname
#os.uname_result
#os.unlink
#os.unsetenv
#os.urandom
#os.utime
#os.wait
#os.wait3
#os.wait4
#os.waitid
#os.waitid_result
#os.waitpid
#os.waitstatus_to_exitcode
#os.walk
#os.write
#os.writev

del os # remover o acesso ao modulo os
