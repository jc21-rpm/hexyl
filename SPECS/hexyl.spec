%global debug_package %{nil}

Name:           hexyl
Version:        0.12.0
Release:        1
Summary:        hexyl is a simple hex viewer for the terminal.
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/sharkdp/%{name}
BuildRequires:  cmake
BuildRequires:  cargo, rust
Source:         https://github.com/sharkdp/%{name}/archive/v%{version}.tar.gz

%description
hexyl is a simple hex viewer for the terminal. It uses a colored output to distinguish
different categories of bytes (NULL bytes, printable ASCII characters, ASCII whitespace
characters, other ASCII characters and non-ASCII).

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/hexyl %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE* *.md
/usr/bin/hexyl

%changelog
* Tue Jan 3 2023 Jamie Curnow <jc@jc21.com> - 0.12.0-1
- v0.12.0

* Wed Dec 7 2022 Jamie Curnow <jc@jc21.com> - 0.11.0-1
- v0.11.0

* Mon May 23 2022 Jamie Curnow <jc@jc21.com> - 0.10.0-1
- v0.10.0

* Mon Jul 12 2021 Jamie Curnow <jc@jc21.com> - 0.9.0-1
- v0.9.0

* Mon Jun 8 2020 Jamie Curnow <jc@jc21.com> - 0.8.0-1
- v0.8.0

* Tue Mar 10 2020 Jamie Curnow <jc@jc21.com> - 0.7.0-1
- v0.7.0

* Wed Oct 9 2019 Jamie Curnow <jc@jc21.com> - 0.6.0-1
- v0.6.0

* Fri May 31 2019 Jamie Curnow <jc@jc21.com> - 0.5.1-1
- v0.5.1

* Sun Apr 14 2019 Jamie Curnow <jc@jc21.com> - 0.5.0-1
- v0.5.0

* Tue Jan 15 2019 Jamie Curnow <jc@jc21.com> - 0.4.0-1
- v0.4.0

* Fri Jan 11 2019 Jamie Curnow <jc@jc21.com> - 0.3.1-1
- Initial spec

