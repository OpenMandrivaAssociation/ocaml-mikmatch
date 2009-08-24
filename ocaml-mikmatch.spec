Name:           ocaml-mikmatch
Version:        1.0.2
Release:        %mkrel 1
Summary:        OCaml extension for pattern matching with regexps

Group:          Development/Other
License:        BSD
URL:            http://martin.jambon.free.fr/micmatch.html
Source0:        http://martin.jambon.free.fr/mikmatch-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

BuildRequires:  ocaml >= 3.11.0
BuildRequires:  ocaml-findlib
BuildRequires:  camlp4
BuildRequires:  ocaml-pcre-devel
BuildRequires:  pcre-devel
BuildRequires:  libncurses-devel

#define _use_internal_dependency_generator 0
#define __find_requires /usr/lib/rpm/ocaml-find-requires.sh
#define __find_provides /usr/lib/rpm/ocaml-find-provides.sh -i Charset -i Constants -i Global_def -i Match -i Messages -i Mm_util -i Pa_mikmatch_pcre -i Pa_mikmatch_str -i Pcre_lib -i Regexp_ast -i Select_lib -i Str_lib -i Syntax_common -i Syntax_pcre -i Syntax_str


%description
Mikmatch (with a 'k') is the OCaml >= 3.10 version of Micmatch, an
extension for adding pattern matching with regular expressions to the
language.

The goal of Micmatch/Mikmatch is to make text-oriented programs even
easier to write, read and run without losing the unique and powerful
features of Objective Caml (OCaml).

Micmatch/Mikmatch provides a concise and highly readable syntax for
regular expressions, and integrates it into the syntax of OCaml thanks
to Camlp4.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}


%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n mikmatch-%{version}


%build
make all str pcre
make opt


%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR $OCAMLFIND_DESTDIR/stublibs
make install-str install-pcre


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE
%{_libdir}/ocaml/mikmatch_str
%{_libdir}/ocaml/mikmatch_pcre
%exclude %{_libdir}/ocaml/mikmatch_str/*.a
%exclude %{_libdir}/ocaml/mikmatch_str/*.cmxa
%exclude %{_libdir}/ocaml/mikmatch_str/*.cmx
%exclude %{_libdir}/ocaml/mikmatch_pcre/*.a
%exclude %{_libdir}/ocaml/mikmatch_pcre/*.cmxa
%exclude %{_libdir}/ocaml/mikmatch_pcre/*.cmx
%exclude %{_libdir}/ocaml/mikmatch_str/*.mli
%exclude %{_libdir}/ocaml/mikmatch_pcre/*.mli


%files devel
%defattr(-,root,root,-)
%doc LICENSE README
%{_libdir}/ocaml/mikmatch_str/*.a
%{_libdir}/ocaml/mikmatch_str/*.cmxa
%{_libdir}/ocaml/mikmatch_str/*.cmx
%{_libdir}/ocaml/mikmatch_pcre/*.a
%{_libdir}/ocaml/mikmatch_pcre/*.cmxa
%{_libdir}/ocaml/mikmatch_pcre/*.cmx
%{_libdir}/ocaml/mikmatch_str/*.mli
%{_libdir}/ocaml/mikmatch_pcre/*.mli


