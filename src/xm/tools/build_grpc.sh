#!/usr/bin/env bash
pushd . > /dev/null
cd $( dirname "${BASH_SOURCE[0]}" )
cd ..

python -m grpc_tools.protoc -I=xm/protos --python_out=xm/generated --grpc_python_out=xm/generated xm/protos/xm.proto
python -m grpc_tools.protoc -I=xm/protos/xm.proto -I=xm/protos --python_out=xm/generated --grpc_python_out=xm/generated xm/protos/xmlegacy.proto
python -m grpc_tools.protoc -I=xm/protos --python_out=xm/generated --grpc_python_out=xm/generated xm/protos/xmbase.proto
python -m grpc_tools.protoc -I=xm/protos --python_out=xm/generated --grpc_python_out=xm/generated xm/protos/xmmining.proto

# Patch import problem in generated code
sed -i 's|import xm_pb2 as xm__pb2|import xm.generated.xm_pb2 as xm__pb2|g' xm/generated/xm_pb2_grpc.py
sed -i 's|import xm_pb2 as xm__pb2|import xm.generated.xm_pb2 as xm__pb2|g' xm/generated/xmlegacy_pb2.py
sed -i 's|import xm_pb2 as xm__pb2|import xm.generated.xm_pb2 as xm__pb2|g' xm/generated/xmmining_pb2.py

sed -i 's|import xmlegacy_pb2 as xmlegacy__pb2|import xm.generated.xmlegacy_pb2 as xmlegacy__pb2|g' xm/generated/xmlegacy_pb2_grpc.py
sed -i 's|import xmbase_pb2 as xmbase__pb2|import xm.generated.xmbase_pb2 as xmbase__pb2|g' xm/generated/xmbase_pb2_grpc.py
sed -i 's|import xmmining_pb2 as xmmining__pb2|import xm.generated.xmmining_pb2 as xmmining__pb2|g' xm/generated/xmmining_pb2_grpc.py

find xm/generated -name '*.py'|grep -v migrations|xargs autoflake --in-place

#docker run --rm \
#  -v $(pwd)/docs/proto:/out \
#  -v $(pwd)/xm/protos:/protos \
#  pseudomuto/protoc-gen-doc --doc_opt=markdown,proto.md
#
#docker run --rm \
#  -v $(pwd)/docs/proto:/out \
#  -v $(pwd)/xm/protos:/protos \
#  pseudomuto/protoc-gen-doc --doc_opt=html,index.html

popd > /dev/null
