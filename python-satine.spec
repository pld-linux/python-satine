# TODO: descriptions
%include        /usr/lib/rpm/macros.python
%define		module Satine
%define		_beta beta-1
Summary:	A Python module
Summary(pl):	Modu³ pythona
Name:		python-%{module}
Version:	1.0
Release:	0.beta.1
License:	GPL
Group:		Libraries/Python
# Source0-md5:	18a153cc9ed3cd45416d8461911029a2
Source0:	http://dl.sourceforge.net/satine/%{module}-%{version}_%{_beta}.zip
URL:		http://satine.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl

%prep
%setup -q -n %{module}-%{version}_%{_beta}

%build
#python config_unix.py \
#	--prefix %{_prefix}
python setup.py config
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGE doc/* examples
%dir %{py_sitedir}/satine
%attr(755,root,root) %{py_sitedir}/satine/*.so
%{py_sitedir}/satine/*.py[co]
%dir %{py_sitedir}/satine/test
%{py_sitedir}/satine/test/*.py[co]
%dir %{py_sitedir}/satine/schemas
%{py_sitedir}/satine/schemas/*.py[co]
%dir %{py_sitedir}/satine/grapes
%{py_sitedir}/satine/grapes/*.py[co]
