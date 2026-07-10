%global tl_name ctanbib
%global tl_revision 79157

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2e
Release:	%{tl_revision}.1
Summary:	Export CTAN entries to bib format
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/ctanbib
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanbib.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ctanbib.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(ctanbib.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a Lua script which can be used for retrieving
bibliographic information in BibLaTeX format for packages hosted on
CTAN. The ctanbib script depends only on LuaXML.

