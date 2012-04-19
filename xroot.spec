Name:           xroot
Version:        0.0.3
Release:        1%{?dist}
Summary:        Tool for quick and easy elevate privileges to root

License:        GPLv2
URL:            http://code.google.com/p/xroot/
Source0:        http://xroot.googlecode.com/files/xroot-src-0.0.3.tar.gz

BuildRequires:  libX11-devel
BuildRequires:  gcc
BuildRequires:  fpc-src >= 2.4.2
BuildRequires:  fpc >= 2.4.2
BuildRequires:  unzip
BuildRequires:  wget


%description
Simple X gui "su/sudo" utility frontend. It is writing on FreePascal
and MSEide+MSEgui.

%prep
%setup -q -n %{name}-src-%{version}


%build
%ifarch x86_64
./build_xroot_without_gui_64
%else
./build_xroot_without_gui_32
%endif


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
cp -f ./xroot/%{name} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -f ./%{name}.png %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/applications
cp -f ./%{name}.desktop %{buildroot}%{_datadir}/applications/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root, root)
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop


%changelog
