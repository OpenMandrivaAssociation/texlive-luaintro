Name:		texlive-luaintro
Version:	0.03
Release:	1
Summary:	Examples from the book "Einfuhrung in LuaTeX und LuaLaTeX"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/examples/luaintro
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaintro.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaintro.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
