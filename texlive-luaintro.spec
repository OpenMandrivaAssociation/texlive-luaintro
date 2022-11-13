Name:		texlive-luaintro
Version:	35490
Release:	1
Summary:	Examples from the book "Einfuhrung in LuaTeX und LuaLaTeX"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/examples/luaintro
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaintro.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaintro.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The bundle provides source of all the examples published in the
German book "Einfuhrung in LuaTeX und LuaLaTeX", published by
Lehmans Media and DANTE, Berlin.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/luatex/luaintro

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
