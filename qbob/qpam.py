"""Define the ProgramArchitect class."""

from pathlib import Path
from textwrap import dedent, indent
from typing import List, Union

from qbob.qbob import OperationBuilder
from qbob.formatter import QSharpFormatter


class ProgramArchitect:

    _QS_FILE_TEMPLATE = \
        """namespace {namespace}
        {{
            open Microsoft.Quantum.Canon;
            open Microsoft.Quantum.Intrinsic;
            {operations}
        }}"""

    def __init__(self, project_name: str, executable: bool = True):
        self.project_name = project_name
        self.operations = []
        self.is_executable = executable

    @property
    def default_csproj_filename(self) -> str:
        return f"{self.project_name}.csproj"

    @property
    def default_qs_filename(self) -> str:
        if self.is_executable:
            return "Program.qs"
        return "Library.qs"

    @property
    def msbuild_properties(self) -> str:
        if self.is_executable:
            return """<OutputType>Exe</OutputType>
                    <TargetFramework>netcoreapp3.1</TargetFramework>"""
        return "<TargetFramework>netstandard2.1</TargetFramework>"

    def create_project(self, folder_path: Union[str, Path]) -> str:
        if isinstance(folder_path, str):
            folder_path = Path(folder_path)

        project_path = self.save_csproj_file(folder_path, self.default_csproj_filename)
        if self.operations:
            self.save_qs_file(folder_path, self.default_qs_filename)

        return str(project_path)

    def save_csproj_file(self, folder_path: Union[str, Path], filename: str) -> str:
        if isinstance(folder_path, str):
            folder_path = Path(folder_path)

        project_path = folder_path / filename
        project_path.write_text(dedent(f"""
            <Project Sdk="Microsoft.Quantum.Sdk/0.14.2011120240">
                <PropertyGroup>
                    {self.msbuild_properties}
                </PropertyGroup>
            </Project>
        """).strip())

        return str(project_path)

    def save_qs_file(self, folder_path: Union[str, Path], filename: str) -> str:
        if isinstance(folder_path, str):
            folder_path = Path(folder_path)

        unformatted_code = self._QS_FILE_TEMPLATE.format(
            namespace=self.project_name,
            operations="".join([op.build() for op in self.operations])
        )

        formatter = QSharpFormatter()
        qs_file_contents = formatter.format_input(unformatted_code)

        qs_file_path = folder_path / filename
        qs_file_path.write_text(qs_file_contents)

        return str(qs_file_path)

    def add_operations(self, *operation_builders: List[OperationBuilder]) -> None:
        self.operations.extend(operation_builders)
