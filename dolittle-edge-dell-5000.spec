Name     : dolittle-edge-dell-5000
Version  : 1.0.0
Release  : 1
License  : MIT
Summary  : Dolittle Edge Dell 5000
URL      : https://github.com/dolittle-edge/dolittle-edge-clearlinux
Source0  : ./static-ip.network

%description

%prep

%build

%install
install -D -m 644 %{SOURCE0} %{buildroot}/usr/lib/systemd/network/70-static-ip-second-nic.network

%post

%preun

%postun

%files
%defattr(-, root, root, -)

# conf
/usr/lib/systemd/network/70-static-ip-second-nic.network

%changelog

