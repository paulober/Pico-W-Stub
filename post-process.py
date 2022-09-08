import json
import os
import shutil
from pathlib import Path

def main():
    folder_path = Path(os.path.dirname(os.path.realpath(__file__)))
    print('  Working with ' + str(folder_path) + ' ...')

    folder_name = folder_path.name
    
    generated_path = folder_path.joinpath("generated")
    frozen_path = folder_path.joinpath("frozen")
    dist_path = folder_path.joinpath("dist")
    micropy_path = dist_path.joinpath("micropy-cli")
    pylance_path = dist_path.joinpath("pylance")

    print('  Processing Micropy-CLI ...')

    if os.path.exists(micropy_path):
        shutil.rmtree(micropy_path)

    os.mkdir(micropy_path)
    os.mkdir(micropy_path.joinpath("stubs"))

    # Create info.json by copying modules.json
    shutil.copyfile(generated_path.joinpath("modules.json"), micropy_path.joinpath("info.json"))

    # Set a "firmware/firmware" value in the JSON
    process_json(str(micropy_path.joinpath("info.json")))

    # Copy the frozen modules
    shutil.copytree(folder_path.joinpath("frozen"), micropy_path.joinpath("frozen"))

    # Rename all .pyi files to .py
    files = micropy_path.glob("**/*.pyi")
    
    for file in files:
        os.rename(file, str(file).replace(".pyi", ".py"))

    # Write version file
    write_version_file(folder_path.joinpath("package.json"), micropy_path.joinpath("version.json"))

    print('  Processing Pylance ...')

    if os.path.exists(pylance_path):
        shutil.rmtree(pylance_path)

    os.mkdir(pylance_path)
    os.mkdir(pylance_path.joinpath("stdlib"))
    os.mkdir(pylance_path.joinpath("stubs"))

    # Write version file
    write_version_file(folder_path.joinpath("package.json"), pylance_path.joinpath("version.json"))

    # Copy frozen items to their respective destinations
    # stdlib

    # The 8 below are from python/typeshed for builtins to work
    shutil.copytree(frozen_path.joinpath("_typeshed"), pylance_path.joinpath("stdlib", "_typeshed"))
    shutil.copytree(frozen_path.joinpath("collections"), pylance_path.joinpath("stdlib", "collections"))
    shutil.copytree(frozen_path.joinpath("importlib"), pylance_path.joinpath("stdlib", "importlib"))
    
    shutil.copyfile(frozen_path.joinpath("_ast.pyi"), pylance_path.joinpath("stdlib", "_ast.pyi"))
    shutil.copyfile(frozen_path.joinpath("_collections_abc.pyi"), pylance_path.joinpath("stdlib", "_collections_abc.pyi"))
    #| Not sure if this is needed
    #|shutil.copyfile(frozen_path.joinpath("_importlib_modulespec.pyi"), pylance_path.joinpath("stdlib", "_importlib_modulespec.pyi"))
    shutil.copyfile(frozen_path.joinpath("abc.pyi"), pylance_path.joinpath("stdlib", "abc.pyi"))
    shutil.copyfile(frozen_path.joinpath("ast.pyi"), pylance_path.joinpath("stdlib", "ast.pyi"))
    # END

    shutil.copyfile(frozen_path.joinpath("_thread.pyi"), pylance_path.joinpath("stdlib", "_thread.pyi"))
    shutil.copyfile(frozen_path.joinpath("array.pyi"), pylance_path.joinpath("stdlib", "array.pyi"))
    shutil.copyfile(frozen_path.joinpath("binascii.pyi"), pylance_path.joinpath("stdlib", "binascii.pyi"))
    shutil.copyfile(frozen_path.joinpath("builtins.pyi"), pylance_path.joinpath("stdlib", "builtins.pyi"))
    shutil.copyfile(frozen_path.joinpath("cmath.pyi"), pylance_path.joinpath("stdlib", "cmath.pyi"))
    shutil.copyfile(frozen_path.joinpath("errno.pyi"), pylance_path.joinpath("stdlib", "errno.pyi"))
    shutil.copyfile(frozen_path.joinpath("gc.pyi"), pylance_path.joinpath("stdlib", "gc.pyi"))
    shutil.copyfile(frozen_path.joinpath("hashlib.pyi"), pylance_path.joinpath("stdlib", "hashlib.pyi"))
    shutil.copyfile(frozen_path.joinpath("heapq.pyi"), pylance_path.joinpath("stdlib", "heapq.pyi"))
    shutil.copyfile(frozen_path.joinpath("io.pyi"), pylance_path.joinpath("stdlib", "io.pyi"))
    shutil.copyfile(frozen_path.joinpath("math.pyi"), pylance_path.joinpath("stdlib", "math.pyi"))
    # The 1 below is from python/typeshed for builtins to work
    shutil.copyfile(frozen_path.joinpath("mmap.pyi"), pylance_path.joinpath("stdlib", "mmap.pyi"))
    # END
    shutil.copyfile(frozen_path.joinpath("os.pyi"), pylance_path.joinpath("stdlib", "os.pyi"))
    shutil.copyfile(frozen_path.joinpath("random.pyi"), pylance_path.joinpath("stdlib", "random.pyi"))
    shutil.copyfile(frozen_path.joinpath("re.pyi"), pylance_path.joinpath("stdlib", "re.pyi"))
    shutil.copyfile(frozen_path.joinpath("select.pyi"), pylance_path.joinpath("stdlib", "select.pyi"))
    shutil.copyfile(frozen_path.joinpath("socket.pyi"), pylance_path.joinpath("stdlib", "socket.pyi"))
    shutil.copyfile(frozen_path.joinpath("ssl.pyi"), pylance_path.joinpath("stdlib", "ssl.pyi"))
    shutil.copyfile(frozen_path.joinpath("struct.pyi"), pylance_path.joinpath("stdlib", "struct.pyi"))
    shutil.copyfile(frozen_path.joinpath("sys.pyi"), pylance_path.joinpath("stdlib", "sys.pyi"))
    shutil.copyfile(frozen_path.joinpath("time.pyi"), pylance_path.joinpath("stdlib", "time.pyi"))
    # The 2 below are from python/typeshed for builtins to work
    shutil.copyfile(frozen_path.joinpath("types.pyi"), pylance_path.joinpath("stdlib", "types.pyi"))
    shutil.copyfile(frozen_path.joinpath("typing.pyi"), pylance_path.joinpath("stdlib", "typing.pyi"))
    # END
    shutil.copyfile(frozen_path.joinpath("uarray.pyi"), pylance_path.joinpath("stdlib", "uarray.pyi"))
    shutil.copyfile(frozen_path.joinpath("ubinascii.pyi"), pylance_path.joinpath("stdlib", "ubinascii.pyi"))
    shutil.copyfile(frozen_path.joinpath("ucollections.pyi"), pylance_path.joinpath("stdlib", "ucollections.pyi"))
    shutil.copyfile(frozen_path.joinpath("uerrno.pyi"), pylance_path.joinpath("stdlib", "uerrno.pyi"))
    shutil.copyfile(frozen_path.joinpath("uhashlib.pyi"), pylance_path.joinpath("stdlib", "uhashlib.pyi"))
    shutil.copyfile(frozen_path.joinpath("uheapq.pyi"), pylance_path.joinpath("stdlib", "uheapq.pyi"))
    shutil.copyfile(frozen_path.joinpath("uio.pyi"), pylance_path.joinpath("stdlib", "uio.pyi"))
    shutil.copyfile(frozen_path.joinpath("uos.pyi"), pylance_path.joinpath("stdlib", "uos.pyi"))
    shutil.copyfile(frozen_path.joinpath("urandom.pyi"), pylance_path.joinpath("stdlib", "urandom.pyi"))
    shutil.copyfile(frozen_path.joinpath("ure.pyi"), pylance_path.joinpath("stdlib", "ure.pyi"))
    shutil.copyfile(frozen_path.joinpath("uselect.pyi"), pylance_path.joinpath("stdlib", "uselect.pyi"))
    shutil.copyfile(frozen_path.joinpath("usocket.pyi"), pylance_path.joinpath("stdlib", "usocket.pyi"))
    shutil.copyfile(frozen_path.joinpath("ussl.pyi"), pylance_path.joinpath("stdlib", "ussl.pyi"))
    shutil.copyfile(frozen_path.joinpath("ustruct.pyi"), pylance_path.joinpath("stdlib", "ustruct.pyi"))
    shutil.copyfile(frozen_path.joinpath("usys.pyi"), pylance_path.joinpath("stdlib", "usys.pyi"))
    shutil.copyfile(frozen_path.joinpath("utime.pyi"), pylance_path.joinpath("stdlib", "utime.pyi"))
    shutil.copyfile(frozen_path.joinpath("uzlib.pyi"), pylance_path.joinpath("stdlib", "uzlib.pyi"))
    shutil.copyfile(frozen_path.joinpath("zlib.pyi"), pylance_path.joinpath("stdlib", "zlib.pyi"))

    # stubs
    shutil.copytree(frozen_path.joinpath("uasyncio"), pylance_path.joinpath("stubs", "uasyncio"))
    
    #|Not intended for public use
    #|copy_to_pylance_folder(frozen_path.joinpath("_onewire.pyi"), pylance_path)
    
    #|Does not exist in this firmware
    #|copy_to_pylance_folder(frozen_path.joinpath("btree.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("dht.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("ds18x20.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("framebuf.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("json.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("lwip.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("machine.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("micropython.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("neopixel.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("network.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("ntptime.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("onewire.pyi"), pylance_path)

    #|Not intended for public use
    #|copy_to_pylance_folder(frozen_path.joinpath("_rp2.pyi"), pylance_path)

    copy_to_pylance_folder(frozen_path.joinpath("rp2.pyi"), pylance_path)

    # TODO: maybe transfer the asyncio stubs to the stdlib section because it's mentioned as stdlib in micropython docs
    #|Does not exist - splited into sperate folder
    #|copy_to_pylance_folder(frozen_path.joinpath("uasyncio.pyi"), pylance_path)

    # The 1 below is from python/typeshed for builtins to work
    copy_to_pylance_folder(frozen_path.joinpath("typing_extensions.pyi"), pylance_path)
    # END
    copy_to_pylance_folder(frozen_path.joinpath("ucryptolib.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("uctypes.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("ujson.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("upip_utarfile.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("urequests.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("uwebsocket.pyi"), pylance_path)
    copy_to_pylance_folder(frozen_path.joinpath("websocket.pyi"), pylance_path)

def process_json(file):
    data = None

    with open(file) as input_file:
        data = json.load(input_file)

    data['firmware']['firmware'] = data['firmware']['platform'] + ' v' + data['firmware']['version']

    with open(file, 'w+') as output_file:
        json.dump(data, output_file)

def copy_to_pylance_folder(frozen_file: Path, pylance_path: Path):
    folder_name = frozen_file.name.replace(".pyi", "")
    try:
        os.mkdir(pylance_path.joinpath("stubs", folder_name))
    except FileExistsError:
        print(folder_name + " already exists!")
    shutil.copyfile(frozen_file, pylance_path.joinpath("stubs", folder_name, frozen_file.name))

def write_version_file(package_path: Path, destination_path: Path):
    pkg = None

    with open(str(package_path)) as input_file:
        pkg = json.load(input_file)

    vers = {}
    vers['version'] = pkg['version']

    with open(str(destination_path), 'w+') as output_file:
        json.dump(vers, output_file)

if __name__ == "__main__":
    main()
