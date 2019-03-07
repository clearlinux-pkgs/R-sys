#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sys
Version  : 3.0
Release  : 3
URL      : https://cran.r-project.org/src/contrib/sys_3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sys_3.0.tar.gz
Summary  : Powerful and Reliable Tools for Running System Commands in R
Group    : Development/Tools
License  : MIT
Requires: R-sys-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
and consistent behavior across platforms. Supports clean interruption, timeout, 
    background tasks, and streaming STDIN / STDOUT / STDERR over binary or text 
    connections. Arguments on Windows automatically get encoded and quoted to work 
    on different locales.

%package lib
Summary: lib components for the R-sys package.
Group: Libraries

%description lib
lib components for the R-sys package.


%prep
%setup -q -c -n sys

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551129606

%install
export SOURCE_DATE_EPOCH=1551129606
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sys
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sys
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sys
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library sys|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sys/DESCRIPTION
/usr/lib64/R/library/sys/INDEX
/usr/lib64/R/library/sys/LICENSE
/usr/lib64/R/library/sys/Meta/Rd.rds
/usr/lib64/R/library/sys/Meta/features.rds
/usr/lib64/R/library/sys/Meta/hsearch.rds
/usr/lib64/R/library/sys/Meta/links.rds
/usr/lib64/R/library/sys/Meta/nsInfo.rds
/usr/lib64/R/library/sys/Meta/package.rds
/usr/lib64/R/library/sys/NAMESPACE
/usr/lib64/R/library/sys/NEWS
/usr/lib64/R/library/sys/R/sys
/usr/lib64/R/library/sys/R/sys.rdb
/usr/lib64/R/library/sys/R/sys.rdx
/usr/lib64/R/library/sys/WORDLIST
/usr/lib64/R/library/sys/help/AnIndex
/usr/lib64/R/library/sys/help/aliases.rds
/usr/lib64/R/library/sys/help/paths.rds
/usr/lib64/R/library/sys/help/sys.rdb
/usr/lib64/R/library/sys/help/sys.rdx
/usr/lib64/R/library/sys/html/00Index.html
/usr/lib64/R/library/sys/html/R.css
/usr/lib64/R/library/sys/libs/symbols.rds
/usr/lib64/R/library/sys/utf8.txt

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sys/libs/sys.so
/usr/lib64/R/library/sys/libs/sys.so.avx2
/usr/lib64/R/library/sys/libs/sys.so.avx512
