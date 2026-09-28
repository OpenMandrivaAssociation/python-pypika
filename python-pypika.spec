Name:		python-pypika
Version:	0.48.9
Release:	1
Summary:	SQL query builder, Frappe fork
License:	Apache-2.0
Group:		Development/Python
URL:		https://pypi.org/project/pypika/
Source0:	pypika-2c50e614.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch
%description
SQL query builder, Frappe fork.

%files
%{py_sitedir}/*
