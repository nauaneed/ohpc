#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the OpenHPC project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#----------------------------------------------------------------------------eh-

%undefine compiler_family
%undefine mpi_family
%undefine python_family
%define ohpc_python_dependent 1

%include %{_sourcedir}/OHPC_macros

Summary: Meta-packages to ease installation
Name:    meta-packages
Version: 2.0
Release: 1
License: Apache-2.0
Group:   %{PROJ_NAME}/meta-package
URL:     https://github.com/openhpc/ohpc
Source0: LICENSE


%description

This is an internal package that is used to create groups as part
of the installation source setup.  Installation of this package does
not make sense.

%package -n %{PROJ_NAME}-autotools
Summary:   OpenHPC autotools
Requires:  autoconf%{PROJ_DELIM}
Requires:  automake%{PROJ_DELIM}
Requires:  libtool%{PROJ_DELIM}
%description -n %{PROJ_NAME}-autotools
Collection of GNU autotools packages

%package -n %{PROJ_NAME}-base
Summary:   OpenHPC base
Requires:  bc
Requires:  conman%{PROJ_DELIM}
Requires:  cmake%{PROJ_DELIM}
Requires:  emacs-nox
Requires:  examples%{PROJ_DELIM}
Requires:  gdb
Requires:  ipmitool
Requires:  libstdc++-devel
Requires:  libunwind
Requires:  lmod%{PROJ_DELIM}
Requires:  losf%{PROJ_DELIM}
Requires:  make
Requires:  man
Requires:  wget
Requires:  net-tools
Requires:  nfs-utils
Requires:  chrony
Requires:  rsyslog
Requires:  OpenIPMI
Requires:  pdsh%{PROJ_DELIM}
Requires:  screen
Requires:  sudo
Requires:  binutils
Requires:  binutils-devel
%if 0%{?rhel}
Requires:  man-db
Requires:  yum-utils
%endif
%if 0%{?suse_version}
Requires:  glibc-locale
Requires:  nfs-kernel-server
%endif
%description -n %{PROJ_NAME}-base
Collection of base packages

%package -n %{PROJ_NAME}-base-compute
Summary:   OpenHPC compute node base
Requires:  binutils
Requires:  libicu
Requires:  libunwind
Requires:  numactl
Requires:  python3
%if 0%{?rhel}
Requires:  cairo-devel
Requires:  libpciaccess
Requires:  libseccomp
%endif
%if 0%{?suse_version}
Requires:  libcairo2
Requires:  libpciaccess0
%endif
%description -n %{PROJ_NAME}-base-compute
Collection of compute node base packages

%package -n %{PROJ_NAME}-ganglia
Summary:   OpenHPC Ganglia monitoring
Requires:  ganglia%{PROJ_DELIM}
Requires:  ganglia-devel%{PROJ_DELIM}
Requires:  ganglia-gmetad%{PROJ_DELIM}
Requires:  ganglia-gmond%{PROJ_DELIM}
Requires:  ganglia-gmond-python%{PROJ_DELIM}
Requires:  ganglia-web%{PROJ_DELIM}
%description -n %{PROJ_NAME}-ganglia
Collection of Ganglia monitoring and metrics packages

%package -n %{PROJ_NAME}-%{compiler_family}-geopm
Summary:   OpenHPC GEOPM power management for GNU
Requires:  geopm-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  geopm-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  geopm-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-geopm
Global Extensible Open Power Manager for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-%{compiler_family}-io-libs
Summary:   OpenHPC IO libraries for GNU
Requires:  adios-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  adios-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  hdf5-%{compiler_family}%{PROJ_DELIM}
Requires:  netcdf-cxx-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  netcdf-cxx-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  netcdf-fortran-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  netcdf-fortran-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  netcdf-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  netcdf-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  pnetcdf-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  pnetcdf-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  phdf5-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  phdf5-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
%ifnarch aarch64
# TODO Requires:  adios-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  netcdf-cxx-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  netcdf-fortran-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  netcdf-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  pnetcdf-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  phdf5-%{compiler_family}-mvapich2%{PROJ_DELIM}
%endif
%description -n %{PROJ_NAME}-%{compiler_family}-io-libs
Collection of IO library builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-%{compiler_family}-mpich-io-libs
Summary:   OpenHPC IO libraries for GNU and MPICH
Requires:  adios-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  netcdf-cxx-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  netcdf-fortran-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  netcdf-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  pnetcdf-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  phdf5-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  hdf5-%{compiler_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-mpich-io-libs
Collection of IO library builds for use with GNU compiler toolchain and the MPICH runtime

%package -n %{PROJ_NAME}-%{compiler_family}-mvapich2-io-libs
Summary:   OpenHPC IO libraries for GNU and MVAPICH2
Requires:  adios-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  netcdf-cxx-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  netcdf-fortran-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  netcdf-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  pnetcdf-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  phdf5-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  hdf5-%{compiler_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-mvapich2-io-libs
Collection of IO library builds for use with GNU compiler toolchain and the MVAPICH2 runtime

%package -n %{PROJ_NAME}-%{compiler_family}-%{mpi_family}-io-libs
Summary:   OpenHPC IO libraries for GNU and OpenMPI
Requires:  adios-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  netcdf-cxx-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  netcdf-fortran-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  netcdf-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  pnetcdf-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  phdf5-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  hdf5-%{compiler_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-%{mpi_family}-io-libs
Collection of IO library builds for use with GNU compiler toolchain and the OpenMPI runtime

%package -n %{PROJ_NAME}-nagios
Summary:   OpenHPC Nagios monitoring
Requires:  nagios%{PROJ_DELIM}
Requires:  nagios-plugins-all%{PROJ_DELIM}
Requires:  nrpe%{PROJ_DELIM}
%description -n %{PROJ_NAME}-nagios
Collection of Nagios monitoring and metrics packages

%package -n %{PROJ_NAME}-%{compiler_family}-parallel-libs
Summary:   OpenHPC parallel libraries for GNU
Requires:  boost-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  boost-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  fftw-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  fftw-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  hypre-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  hypre-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  mfem-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  mfem-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  mumps-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  mumps-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  petsc-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  petsc-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  opencoarrays-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  opencoarrays-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  scalapack-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  scalapack-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  slepc-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  slepc-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  ptscotch-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  ptscotch-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  superlu_dist-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  superlu_dist-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  trilinos-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  trilinos-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
%ifnarch aarch64
Requires:  boost-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  fftw-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  hypre-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  mfem-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  mumps-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  petsc-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  opencoarrays-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  scalapack-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  slepc-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  ptscotch-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  superlu_dist-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  trilinos-%{compiler_family}-mvapich2%{PROJ_DELIM}
%endif
%description -n %{PROJ_NAME}-%{compiler_family}-parallel-libs
Collection of parallel library builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-%{compiler_family}-mpich-parallel-libs
Summary:   OpenHPC parallel libraries for GNU and MPICH
Requires:  boost-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  fftw-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  hypre-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  mfem-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  mumps-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  petsc-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  opencoarrays-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  scalapack-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  slepc-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  ptscotch-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  superlu_dist-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  trilinos-%{compiler_family}-mpich%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-mpich-parallel-libs
Collection of parallel library builds for use with GNU compiler toolchain and the MPICH runtime

%package -n %{PROJ_NAME}-%{compiler_family}-%{mpi_family}-parallel-libs
Summary:   OpenHPC parallel libraries for GNU and OpenMPI
Requires:  boost-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  fftw-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  hypre-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  mfem-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  mumps-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  petsc-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
%if 0%{?rhel}
Requires:  opencoarrays-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
%endif
Requires:  scalapack-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  slepc-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  ptscotch-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  superlu_dist-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  trilinos-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-%{mpi_family}-parallel-libs
Collection of parallel library builds for use with GNU compiler toolchain and the OpenMPI runtime

%package -n %{PROJ_NAME}-%{compiler_family}-perf-tools
Summary:   OpenHPC performance tools for GNU
%if 0%{?rhel}
Requires:  dimemas-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  dimemas-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
%endif
Requires:  extrae-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  extrae-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires: imb-%{compiler_family}-mpich%{PROJ_DELIM}
Requires: imb-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  omb-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  omb-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  tau-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  tau-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  scalasca-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  scalasca-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  scorep-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  scorep-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
%ifnarch aarch64
%if 0%{?rhel}
Requires:  dimemas-%{compiler_family}-mvapich2%{PROJ_DELIM}
%endif
Requires:  extrae-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires: imb-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  likwid-%{compiler_family}%{PROJ_DELIM}
Requires:  omb-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
Requires:  tau-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  scalasca-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  scorep-%{compiler_family}-mvapich2%{PROJ_DELIM}
%endif
%description -n %{PROJ_NAME}-%{compiler_family}-perf-tools
Collection of performance tool builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-%{compiler_family}-mpich-perf-tools
Summary:   OpenHPC performance tools for GNU and MPICH
%if 0%{?rhel}
Requires:  dimemas-%{compiler_family}-mpich%{PROJ_DELIM}
%endif
Requires:  extrae-%{compiler_family}-mpich%{PROJ_DELIM}
## TODO Requires: imb-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  omb-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  tau-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  scalasca-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  scorep-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-mpich-perf-tools
Collection of performance tool builds for use with GNU compiler toolchain and the MPICH runtime

%package -n %{PROJ_NAME}-%{compiler_family}-mvapich2-perf-tools
Summary:   OpenHPC performance tools for GNU and MVAPICH2
%if 0%{?rhel}
Requires:  dimemas-%{compiler_family}-mvapich2%{PROJ_DELIM}
%endif
Requires:  extrae-%{compiler_family}-mvapich2%{PROJ_DELIM}
## TODO Requires: imb-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  likwid-%{compiler_family}%{PROJ_DELIM}
Requires:  omb-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  tau-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  scalasca-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  scorep-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-mvapich2-perf-tools
Collection of performance tool builds for use with GNU compiler toolchain and the MVAPICH2 runtime

%package -n %{PROJ_NAME}-%{compiler_family}-%{mpi_family}-perf-tools
Summary:   OpenHPC performance tools for GNU and OpenMPI
%if 0%{?rhel}
Requires:  dimemas-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
%endif
Requires:  extrae-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
## TODO Requires: imb-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  likwid-%{compiler_family}%{PROJ_DELIM}
Requires:  omb-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  tau-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  scalasca-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  scorep-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-%{mpi_family}-perf-tools
Collection of performance tool builds for use with GNU compiler toolchain and the OpenMPI runtime

%package -n %{PROJ_NAME}-%{compiler_family}-python-libs
Summary:   OpenHPC python libraries for GNU
Requires:  %{PROJ_NAME}-%{compiler_family}-python3-libs
%description -n %{PROJ_NAME}-%{compiler_family}-python-libs
Collection of python related library builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-%{compiler_family}-python3-libs
Summary:   OpenHPC python3 libraries for GNU
Requires:  %{python_prefix}-mpi4py-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  %{python_prefix}-mpi4py-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
Requires:  %{python_prefix}-numpy-%{compiler_family}%{PROJ_DELIM}
Requires:  %{python_prefix}-scipy-%{compiler_family}-mpich%{PROJ_DELIM}
Requires:  %{python_prefix}-scipy-%{compiler_family}-%{mpi_family}%{PROJ_DELIM}
%ifnarch aarch64
Requires:  %{python_prefix}-mpi4py-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  %{python_prefix}-scipy-%{compiler_family}-mvapich2%{PROJ_DELIM}
%endif
%description -n %{PROJ_NAME}-%{compiler_family}-python3-libs
Collection of python3 related library builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-%{compiler_family}-runtimes
Summary:   OpenHPC runtimes for GNU
#Requires:  ocr-%{compiler_family}%{PROJ_DELIM}
Requires:  charliecloud%{PROJ_DELIM}
Requires:  singularity%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-runtimes
Collection of runtimes for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-%{compiler_family}-serial-libs
Summary:   OpenHPC serial libraries for GNU
Requires:  gsl-%{compiler_family}%{PROJ_DELIM}
Requires:  metis-%{compiler_family}%{PROJ_DELIM}
Requires:  openblas-%{compiler_family}%{PROJ_DELIM}
Requires:  plasma-%{compiler_family}%{PROJ_DELIM}
Requires:  R-%{compiler_family}%{PROJ_DELIM}
Requires:  scotch-%{compiler_family}%{PROJ_DELIM}
Requires:  superlu-%{compiler_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-serial-libs
Collection of serial library builds for use with GNU compiler toolchain

%package -n %{PROJ_NAME}-slurm-client
Summary:   OpenHPC client packages for SLURM
Requires:  slurm%{PROJ_DELIM}
Requires:  slurm-slurmd%{PROJ_DELIM}
Requires:  slurm-contribs%{PROJ_DELIM}
Requires:  slurm-example-configs%{PROJ_DELIM}
Requires:  slurm-pam_slurm%{PROJ_DELIM}
%if 0%{?rhel}
Requires:  hwloc-libs
%endif
%if 0%{?suse_version}
Requires:  libhwloc5
%endif
%description -n %{PROJ_NAME}-slurm-client
Collection of client packages for SLURM

%package -n %{PROJ_NAME}-slurm-server
Summary:   OpenHPC server packages for SLURM
Requires:  slurm%{PROJ_DELIM}
Requires:  slurm-devel%{PROJ_DELIM}
Requires:  slurm-example-configs%{PROJ_DELIM}
Requires:  slurm-perlapi%{PROJ_DELIM}
Requires:  slurm-slurmctld%{PROJ_DELIM}
Requires:  slurm-slurmdbd%{PROJ_DELIM}
Requires:  pdsh-mod-slurm%{PROJ_DELIM}
%description -n %{PROJ_NAME}-slurm-server
Collection of server packages for SLURM

%package -n %{PROJ_NAME}-warewulf
Summary:   OpenHPC base packages for Warewulf
Requires:  warewulf-cluster%{PROJ_DELIM}
Requires:  warewulf-common%{PROJ_DELIM}
Requires:  warewulf-common%{PROJ_DELIM}-localdb
Requires:  warewulf-ipmi%{PROJ_DELIM}
Requires:  warewulf-ipmi%{PROJ_DELIM}-initramfs-%{_arch}
Requires:  warewulf-provision%{PROJ_DELIM}-initramfs-%{_arch}
Requires:  warewulf-provision%{PROJ_DELIM}
Requires:  warewulf-provision%{PROJ_DELIM}-server
Requires:  warewulf-provision%{PROJ_DELIM}-server-ipxe-%{_arch}
Requires:  warewulf-vnfs%{PROJ_DELIM}
%description -n %{PROJ_NAME}-warewulf
Collection of base packages for Warewulf provisioning

# x86_64 specific groups
%ifnarch aarch64
%package -n %{PROJ_NAME}-intel-geopm
Summary:   OpenHPC GEOPM power management for Intel(R) Parallel Studio XE
Requires:  geopm-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  geopm-intel-impi%{PROJ_DELIM}
Requires:  geopm-intel-mpich%{PROJ_DELIM}
Requires:  geopm-intel-mvapich2%{PROJ_DELIM}
Requires:  geopm-intel-%{mpi_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-geopm
Global Extensible Open Power Manager for use with Intel(R) Parallel Studio XE software suite

%package -n %{PROJ_NAME}-intel-io-libs
Summary:   OpenHPC IO libraries for Intel(R) Parallel Studio XE
Requires:  adios-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  adios-intel-impi%{PROJ_DELIM}
Requires:  adios-intel-mpich%{PROJ_DELIM}
Requires:  adios-intel-mvapich2%{PROJ_DELIM}
Requires:  adios-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  hdf5-intel%{PROJ_DELIM}
Requires:  netcdf-cxx-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-impi%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-mpich%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-mvapich2%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  netcdf-fortran-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-impi%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-mpich%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-mvapich2%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  netcdf-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  netcdf-intel-impi%{PROJ_DELIM}
Requires:  netcdf-intel-mpich%{PROJ_DELIM}
Requires:  netcdf-intel-mvapich2%{PROJ_DELIM}
Requires:  netcdf-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  pnetcdf-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  pnetcdf-intel-impi%{PROJ_DELIM}
Requires:  pnetcdf-intel-mpich%{PROJ_DELIM}
Requires:  pnetcdf-intel-mvapich2%{PROJ_DELIM}
Requires:  pnetcdf-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  phdf5-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  phdf5-intel-impi%{PROJ_DELIM}
Requires:  phdf5-intel-mpich%{PROJ_DELIM}
Requires:  phdf5-intel-mvapich2%{PROJ_DELIM}
Requires:  phdf5-intel-%{mpi_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-io-libs
Collection of IO library builds for use with Intel(R) Parallel Studio XE software suite

%package -n %{PROJ_NAME}-intel-impi-io-libs
Summary:   OpenHPC IO libraries for Intel(R) Parallel Studio XE and Intel(R) MPI runtime
Requires:  adios-intel-impi%{PROJ_DELIM}
Requires:  hdf5-intel%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-impi%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-impi%{PROJ_DELIM}
Requires:  netcdf-intel-impi%{PROJ_DELIM}
Requires:  phdf5-intel-impi%{PROJ_DELIM}
Requires:  pnetcdf-intel-impi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-impi-io-libs
Collection of IO library builds for use with Intel(R) Parallel Studio XE software suite and Intel(R) MPI runtime

%package -n %{PROJ_NAME}-intel-mpich-io-libs
Summary:   OpenHPC IO libraries for Intel(R) Parallel Studio XE and MPICH
Requires:  adios-intel-mpich%{PROJ_DELIM}
Requires:  hdf5-intel%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-mpich%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-mpich%{PROJ_DELIM}
Requires:  netcdf-intel-mpich%{PROJ_DELIM}
Requires:  phdf5-intel-mpich%{PROJ_DELIM}
Requires:  pnetcdf-intel-mpich%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-mpich-io-libs
Collection of IO library builds for use with Intel(R) Parallel Studio XE software suite and MPICH runtime

%package -n %{PROJ_NAME}-intel-mvapich2-io-libs
Summary:   OpenHPC IO libraries for Intel(R) Parallel Studio XE and MVAPICH2
Requires:  adios-intel-mvapich2%{PROJ_DELIM}
Requires:  hdf5-intel%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-mvapich2%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-mvapich2%{PROJ_DELIM}
Requires:  netcdf-intel-mvapich2%{PROJ_DELIM}
Requires:  phdf5-intel-mvapich2%{PROJ_DELIM}
Requires:  pnetcdf-intel-mvapich2%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-mvapich2-io-libs
Collection of IO library builds for use with Intel(R) Parallel Studio XE software suite and MVAPICH2 runtime

%package -n %{PROJ_NAME}-intel-%{mpi_family}-io-libs
Summary:   OpenHPC IO libraries for Intel(R) Parallel Studio XE and OpenMPI
Requires:  adios-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  hdf5-intel%{PROJ_DELIM}
Requires:  netcdf-cxx-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  netcdf-fortran-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  netcdf-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  phdf5-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  pnetcdf-intel-%{mpi_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-%{mpi_family}-io-libs
Collection of IO library builds for use with Intel(R) Parallel Studio XE software suite and OpenMPI runtime

%package -n %{PROJ_NAME}-%{compiler_family}-mvapich2-parallel-libs
Summary:   OpenHPC parallel libraries for GNU and MVAPICH2
Requires:  boost-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  fftw-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  hypre-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  mfem-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  mumps-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  petsc-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  opencoarrays-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  scalapack-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  slepc-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  ptscotch-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  superlu_dist-%{compiler_family}-mvapich2%{PROJ_DELIM}
Requires:  trilinos-%{compiler_family}-mvapich2%{PROJ_DELIM}
%description -n %{PROJ_NAME}-%{compiler_family}-mvapich2-parallel-libs
Collection of parallel library builds for use with GNU compiler toolchain and the MVAPICH2 runtime

%package -n %{PROJ_NAME}-intel-impi-parallel-libs
Summary:   OpenHPC parallel libraries for Intel(R) Parallel Studio XE and Intel(R) MPI Library
Requires:  boost-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  boost-intel-impi%{PROJ_DELIM}
Requires:  hypre-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  hypre-intel-impi%{PROJ_DELIM}
## TODO Requires:  mfem-%{compiler_family}-impi%{PROJ_DELIM}
## TODO Requires:  mfem-intel-impi%{PROJ_DELIM}
Requires:  mumps-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  mumps-intel-impi%{PROJ_DELIM}
Requires:  opencoarrays-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  petsc-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  petsc-intel-impi%{PROJ_DELIM}
Requires:  scalapack-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  scalapack-intel-impi%{PROJ_DELIM}
Requires:  slepc-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  slepc-intel-impi%{PROJ_DELIM}
Requires:  ptscotch-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  ptscotch-intel-impi%{PROJ_DELIM}
## TODO Requires:  superlu_dist-%{compiler_family}-impi%{PROJ_DELIM}
## TODO Requires:  superlu_dist-intel-impi%{PROJ_DELIM}
Requires:  trilinos-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  trilinos-intel-impi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-impi-parallel-libs
Collection of parallel library builds for use with Intel(R) Parallel Studio XE toolchain and the Intel(R) MPI Library

%package -n %{PROJ_NAME}-intel-mpich-parallel-libs
Summary:   OpenHPC parallel libraries for Intel(R) Parallel Studio XE and MPICH
Requires:  boost-intel-mpich%{PROJ_DELIM}
Requires:  hypre-intel-mpich%{PROJ_DELIM}
## TODO Requires:  mfem-intel-mpich%{PROJ_DELIM}
Requires:  mumps-intel-mpich%{PROJ_DELIM}
Requires:  petsc-intel-mpich%{PROJ_DELIM}
Requires:  scalapack-intel-mpich%{PROJ_DELIM}
Requires:  slepc-intel-mpich%{PROJ_DELIM}
Requires:  ptscotch-intel-mpich%{PROJ_DELIM}
## TODO Requires:  superlu_dist-intel-mpich%{PROJ_DELIM}
Requires:  trilinos-intel-mpich%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-mpich-parallel-libs
Collection of parallel library builds for use with Intel(R) Parallel Studio XE toolchain and the MPICH runtime

%package -n %{PROJ_NAME}-intel-mvapich2-parallel-libs
Summary:   OpenHPC parallel libraries for Intel(R) Parallel Studio XE and MVAPICH2
Requires:  boost-intel-mvapich2%{PROJ_DELIM}
Requires:  hypre-intel-mvapich2%{PROJ_DELIM}
## TODO Requires:  mfem-intel-mvapich2%{PROJ_DELIM}
Requires:  mumps-intel-mvapich2%{PROJ_DELIM}
Requires:  petsc-intel-mvapich2%{PROJ_DELIM}
Requires:  scalapack-intel-mvapich2%{PROJ_DELIM}
Requires:  slepc-intel-mvapich2%{PROJ_DELIM}
Requires:  ptscotch-intel-mvapich2%{PROJ_DELIM}
## TODO Requires:  superlu_dist-intel-mvapich2%{PROJ_DELIM}
Requires:  trilinos-intel-mvapich2%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-mvapich2-parallel-libs
Collection of parallel library builds for use with Intel(R) Parallel Studio XE toolchain and the MVAPICH2 runtime

%package -n %{PROJ_NAME}-intel-%{mpi_family}-parallel-libs
Summary:   OpenHPC parallel libraries for Intel(R) Parallel Studio XE and OpenMPI
Requires:  boost-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  hypre-intel-%{mpi_family}%{PROJ_DELIM}
## TODO Requires:  mfem-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  mumps-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  petsc-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  scalapack-intel-%{mpi_family}%{PROJ_DELIM}
## TODO Requires:  slepc-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  ptscotch-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  superlu_dist-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  trilinos-intel-%{mpi_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-%{mpi_family}-parallel-libs
Collection of parallel library builds for use with Intel(R) Parallel Studio XE toolchain and the OpenMPI runtime

%package -n %{PROJ_NAME}-intel-perf-tools
Summary:   OpenHPC performance tools for Intel(R) Parallel Studio XE
%if 0%{?rhel}
Requires:  dimemas-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  dimemas-intel-impi%{PROJ_DELIM}
Requires:  dimemas-intel-mpich%{PROJ_DELIM}
Requires:  dimemas-intel-mvapich2%{PROJ_DELIM}
Requires:  dimemas-intel-%{mpi_family}%{PROJ_DELIM}
%endif
Requires:  extrae-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  extrae-intel-impi%{PROJ_DELIM}
Requires:  extrae-intel-mpich%{PROJ_DELIM}
Requires:  extrae-intel-mvapich2%{PROJ_DELIM}
Requires:  extrae-intel-%{mpi_family}%{PROJ_DELIM}
## TODO Requires: imb-%{compiler_family}-impi%{PROJ_DELIM}
## TODO Requires: imb-intel-impi%{PROJ_DELIM}
## TODO Requires: imb-intel-mpich%{PROJ_DELIM}
## TODO Requires: imb-intel-mvapich2%{PROJ_DELIM}
## TODO Requires: imb-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  likwid-intel%{PROJ_DELIM}
Requires:  omb-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  omb-intel-impi%{PROJ_DELIM}
Requires:  omb-intel-mpich%{PROJ_DELIM}
Requires:  omb-intel-mvapich2%{PROJ_DELIM}
Requires:  omb-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
## TODO Requires:  tau-%{compiler_family}-impi%{PROJ_DELIM}
## TODO Requires:  tau-intel-impi%{PROJ_DELIM}
## TODO Requires:  tau-intel-mpich%{PROJ_DELIM}
## TODO Requires:  tau-intel-mvapich2%{PROJ_DELIM}
## TODO Requires:  tau-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  scalasca-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  scalasca-intel-impi%{PROJ_DELIM}
Requires:  scalasca-intel-mpich%{PROJ_DELIM}
Requires:  scalasca-intel-mvapich2%{PROJ_DELIM}
Requires:  scalasca-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  scorep-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  scorep-intel-impi%{PROJ_DELIM}
Requires:  scorep-intel-mpich%{PROJ_DELIM}
Requires:  scorep-intel-mvapich2%{PROJ_DELIM}
Requires:  scorep-intel-%{mpi_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-perf-tools
Collection of performance tool builds for use with Intel(R) Parallel Studio XE toolchain

%package -n %{PROJ_NAME}-intel-impi-perf-tools
Summary:   OpenHPC performance tools for Intel(R) Parallel Studio XE and Intel(R) MPI
## TODO Requires: imb-intel-impi%{PROJ_DELIM}
Requires:  likwid-intel%{PROJ_DELIM}
Requires:  omb-intel-impi%{PROJ_DELIM}
## TODO Requires:  tau-intel-impi%{PROJ_DELIM}
Requires:  scalasca-intel-impi%{PROJ_DELIM}
Requires:  scorep-intel-impi%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-impi-perf-tools
Collection of performance tool builds for use with Intel(R) Parallel Studio XE compiler toolchain and the Intel(R) MPI runtime

%package -n %{PROJ_NAME}-intel-mpich-perf-tools
Summary:   OpenHPC performance tools for Intel(R) Parallel Studio XE and MPICH
## TODO Requires: imb-intel-mpich%{PROJ_DELIM}
Requires:  likwid-intel%{PROJ_DELIM}
Requires:  omb-intel-mpich%{PROJ_DELIM}
## TODO Requires:  tau-intel-mpich%{PROJ_DELIM}
Requires:  scalasca-intel-mpich%{PROJ_DELIM}
Requires:  scorep-intel-mpich%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-mpich-perf-tools
Collection of performance tool builds for use with Intel(R) Parallel Studio XE compiler toolchain and the MPICH runtime

%package -n %{PROJ_NAME}-intel-mvapich2-perf-tools
Summary:   OpenHPC performance tools for Intel(R) Parallel Studio XE and MVAPICH2
## TODO Requires: imb-intel-mvapich2%{PROJ_DELIM}
Requires:  likwid-intel%{PROJ_DELIM}
Requires:  omb-intel-mvapich2%{PROJ_DELIM}
## TODO Requires:  tau-intel-mvapich2%{PROJ_DELIM}
Requires:  scalasca-intel-mvapich2%{PROJ_DELIM}
Requires:  scorep-intel-mvapich2%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-mvapich2-perf-tools
Collection of performance tool builds for use with Intel(R) Parallel Studio XE compiler toolchain and the MVAPICH2 runtime

%package -n %{PROJ_NAME}-intel-%{mpi_family}-perf-tools
Summary:   OpenHPC performance tools for Intel(R) Parallel Studio XE and OpenMPI
## TODO Requires: imb-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  likwid-intel%{PROJ_DELIM}
Requires:  omb-intel-%{mpi_family}%{PROJ_DELIM}
## TODO Requires:  tau-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  scalasca-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  scorep-intel-%{mpi_family}%{PROJ_DELIM}
Requires:  papi%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-%{mpi_family}-perf-tools
Collection of performance tool builds for use with Intel(R) Parallel Studio XE compiler toolchain and the OpenMPI runtime

%package -n %{PROJ_NAME}-intel-python-libs
Summary:   OpenHPC python libraries for Intel(R) Parallel Studio XE
Requires:  %{PROJ_NAME}-intel-python3-libs
%description -n %{PROJ_NAME}-intel-python-libs
Collection of python related library builds for use with Intel(R) Parallel Studio XE toolchain

%package -n %{PROJ_NAME}-intel-python3-libs
Summary:   OpenHPC python3 libraries for Intel(R) Parallel Studio XE
Requires:  %{python_prefix}-numpy-intel%{PROJ_DELIM}
Requires:  %{python_prefix}-mpi4py-%{compiler_family}-impi%{PROJ_DELIM}
Requires:  %{python_prefix}-mpi4py-intel-impi%{PROJ_DELIM}
Requires:  %{python_prefix}-mpi4py-intel-mpich%{PROJ_DELIM}
Requires:  %{python_prefix}-mpi4py-intel-mvapich2%{PROJ_DELIM}
Requires:  %{python_prefix}-mpi4py-intel-%{mpi_family}%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-python3-libs
Collection of python3 related library builds for use with Intel(R) Parallel Studio XE toolchain

%package -n %{PROJ_NAME}-intel-runtimes
Summary:   OpenHPC runtimes for Intel(R) Parallel Studio XE toolchain
#Requires:  ocr-intel%{PROJ_DELIM}
Requires:  charliecloud%{PROJ_DELIM}
Requires:  singularity%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-runtimes
Collection of runtimes for use with Intel(R) Parallel Studio XE toolchain

%package -n %{PROJ_NAME}-intel-serial-libs
Summary:   OpenHPC serial libraries for Intel(R) Parallel Studio XE
Requires:  metis-intel%{PROJ_DELIM}
Requires:  plasma-intel%{PROJ_DELIM}
Requires:  scotch-intel%{PROJ_DELIM}
Requires:  superlu-intel%{PROJ_DELIM}
%description -n %{PROJ_NAME}-intel-serial-libs
Collection of serial library builds for use with Intel(R) Parallel Studio XE toolchain

%endif


%prep
%{__cp} %SOURCE0 .

%build

%install

%{__mkdir_p} ${RPM_BUILD_ROOT}/%{_docdir}

%files

%files -n %{PROJ_NAME}-autotools
%files -n %{PROJ_NAME}-base
%files -n %{PROJ_NAME}-base-compute
%files -n %{PROJ_NAME}-ganglia
%files -n %{PROJ_NAME}-%{compiler_family}-geopm
%files -n %{PROJ_NAME}-%{compiler_family}-io-libs
%files -n %{PROJ_NAME}-%{compiler_family}-mpich-io-libs
%files -n %{PROJ_NAME}-%{compiler_family}-%{mpi_family}-io-libs
%files -n %{PROJ_NAME}-%{compiler_family}-parallel-libs
%files -n %{PROJ_NAME}-%{compiler_family}-mpich-parallel-libs
%files -n %{PROJ_NAME}-%{compiler_family}-%{mpi_family}-parallel-libs
%files -n %{PROJ_NAME}-%{compiler_family}-perf-tools
%files -n %{PROJ_NAME}-%{compiler_family}-mpich-perf-tools
%files -n %{PROJ_NAME}-%{compiler_family}-%{mpi_family}-perf-tools
%files -n %{PROJ_NAME}-%{compiler_family}-python-libs
%files -n %{PROJ_NAME}-%{compiler_family}-python3-libs
%files -n %{PROJ_NAME}-%{compiler_family}-runtimes
%files -n %{PROJ_NAME}-%{compiler_family}-serial-libs
%files -n %{PROJ_NAME}-nagios
%files -n %{PROJ_NAME}-slurm-client
%files -n %{PROJ_NAME}-slurm-server
%files -n %{PROJ_NAME}-warewulf
# x86_64 specific groups
%ifnarch aarch64
%files -n %{PROJ_NAME}-%{compiler_family}-mvapich2-io-libs
%files -n %{PROJ_NAME}-%{compiler_family}-mvapich2-perf-tools
%files -n %{PROJ_NAME}-%{compiler_family}-mvapich2-parallel-libs
%files -n %{PROJ_NAME}-intel-geopm
%files -n %{PROJ_NAME}-intel-io-libs
%files -n %{PROJ_NAME}-intel-impi-io-libs
%files -n %{PROJ_NAME}-intel-mpich-io-libs
%files -n %{PROJ_NAME}-intel-mvapich2-io-libs
%files -n %{PROJ_NAME}-intel-%{mpi_family}-io-libs
%files -n %{PROJ_NAME}-intel-impi-parallel-libs
%files -n %{PROJ_NAME}-intel-mpich-parallel-libs
%files -n %{PROJ_NAME}-intel-mvapich2-parallel-libs
%files -n %{PROJ_NAME}-intel-%{mpi_family}-parallel-libs
%files -n %{PROJ_NAME}-intel-perf-tools
%files -n %{PROJ_NAME}-intel-impi-perf-tools
%files -n %{PROJ_NAME}-intel-mpich-perf-tools
%files -n %{PROJ_NAME}-intel-mvapich2-perf-tools
%files -n %{PROJ_NAME}-intel-%{mpi_family}-perf-tools
%files -n %{PROJ_NAME}-intel-python-libs
%files -n %{PROJ_NAME}-intel-python3-libs
%files -n %{PROJ_NAME}-intel-runtimes
%files -n %{PROJ_NAME}-intel-serial-libs
%endif
