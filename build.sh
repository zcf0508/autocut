# run this script after pyinstaller
# see https://github.com/pyinstaller/pyinstaller/issues/7582#issuecomment-1515434457

cd dist/autocut

rm -f libtorch*
ln -s torch/lib/libtorch.dylib .
ln -s torch/lib/libtorch_cpu.dylib .
ln -s torch/lib/libtorch_python.dylib .

ln -s torchaudio/lib/libtorchaudio.so .

install_name_tool -add_rpath @loader_path/../.. torchaudio/lib/libtorchaudio.so
