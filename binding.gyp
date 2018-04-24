{
  'targets': [
    {
      'target_name': 'exokit',
      'conditions': [
        ['OS=="win"', {
          'sources': [
            'main.cpp',
            'deps/exokit-bindings/bindings/src/*.cc',
            'deps/exokit-bindings/util/src/*.cc',
            'deps/exokit-bindings/canvas/src/*.cpp',
            'deps/exokit-bindings/nanosvg/src/*.cpp',
            'deps/exokit-bindings/canvascontext/src/*.cc',
            'deps/exokit-bindings/webglcontext/src/*.cc',
            'deps/exokit-bindings/platform/windows/src/*.cpp',
            'deps/exokit-bindings/webaudiocontext/src/*.cpp',
            'deps/exokit-bindings/videocontext/src/*.cpp',
            'deps/exokit-bindings/glfw/src/*.cc',
            'deps/openvr/src/*.cpp',
          ],
          'include_dirs': [
            '<(module_root_dir)/node_modules/native-graphics-deps/include',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/core',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/config',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/gpu',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/effects',
            '<(module_root_dir)/node_modules/native-audio-deps/include',
            '<(module_root_dir)/node_modules/native-video-deps/include',
            '<(module_root_dir)/node_modules/native-openvr-deps/headers',
            '<(module_root_dir)/deps/exokit-bindings',
            '<(module_root_dir)/deps/exokit-bindings/utf8',
            '<(module_root_dir)/deps/exokit-bindings/node',
            '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
            '<(module_root_dir)/deps/exokit-bindings/util/include',
            '<(module_root_dir)/deps/exokit-bindings/bindings/include',
            '<(module_root_dir)/deps/exokit-bindings/canvas/include',
            '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
            '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/glfw/include',
            '<(module_root_dir)/deps/openvr/include',
          ],
          'library_dirs': [
            '<(module_root_dir)/node_modules/native-graphics-deps/lib/windows/glew',
            '<(module_root_dir)/node_modules/native-graphics-deps/lib/windows/glfw',
            '<(module_root_dir)/node_modules/native-canvas-deps/lib/windows',
            '<(module_root_dir)/node_modules/native-audio-deps/lib/windows',
            '<(module_root_dir)/node_modules/native-video-deps/lib/win',
            '<(module_root_dir)/node_modules/native-openvr-deps/lib/win64',
            '<(module_root_dir)/node_modules/magicleap/lib/win64',
          ],
          'libraries': [
            'opengl32.lib',
            'glew32.lib',
            'glfw3dll.lib',
            'gdiplus.lib',
            'skia.lib',
            'LabSound.lib',
            'avformat.lib',
            'avcodec.lib',
            'avutil.lib',
            'swscale.lib',
            'swresample.lib',
            'openvr_api.lib',
          ],
          'copies': [
            {
              'destination': '<(module_root_dir)/build/Release/',
              'files': [
                '<(module_root_dir)/node_modules/native-graphics-deps/lib/windows/glew/glew32.dll',
                '<(module_root_dir)/node_modules/native-graphics-deps/lib/windows/glfw/glfw3.dll',
                '<(module_root_dir)/node_modules/native-video-deps/lib/win/avformat-58.dll',
                '<(module_root_dir)/node_modules/native-video-deps/lib/win/avcodec-58.dll',
                '<(module_root_dir)/node_modules/native-video-deps/lib/win/avutil-56.dll',
                '<(module_root_dir)/node_modules/native-video-deps/lib/win/swscale-5.dll',
                '<(module_root_dir)/node_modules/native-video-deps/lib/win/swresample-3.dll',
                '<(module_root_dir)/node_modules/native-openvr-deps/bin/win64/openvr_api.dll',
              ]
            }
          ],
          'defines': [
            'NOMINMAX',
          ],
          'conditions': [
            ['"<!(echo %MAGICLEAP%)" != "%MAGICLEAP%"', {
              'sources': [
                'deps/exokit-bindings/magicleap/src/*.cc',
              ],
              'include_dirs': [
                '<(module_root_dir)/deps/exokit-bindings/magicleap/include',
                '<(module_root_dir)/node_modules/magicleap/include',
              ],
              'libraries': [
                'ml_app_analytics.lib',
                'ml_audio.lib',
                'ml_camera.lib',
                'ml_camera_metadata.lib',
                'ml_dispatch.lib',
                'ml_ext_logging.lib',
                'ml_graphics.lib',
                'ml_identity.lib',
                'ml_input.lib',
                'ml_lifecycle.lib',
                'ml_mediacodec.lib',
                'ml_mediacodeclist.lib',
                'ml_mediacrypto.lib',
                'ml_mediadrm.lib',
                'ml_mediaerror.lib',
                'ml_mediaextractor.lib',
                'ml_mediaformat.lib',
                'ml_mediaplayer.lib',
                'ml_musicservice.lib',
                'ml_perception_client.lib',
                'ml_privileges.lib',
                'ml_screens.lib',
                'ml_secure_storage.lib',
                'ml_sharedfile.lib',
              ],
              'copies': [
                {
                  'destination': '<(module_root_dir)/build/Release/',
                  'files': [
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/assimp-vc140-mt.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/GesturesMixer.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/glfw3.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/InputControllerMixer.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_app_analytics.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_audio.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_camera.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_camera_metadata.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_dispatch.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_ext_logging.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_graphics.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_identity.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_input.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_lifecycle.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_mediacodec.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_mediacodeclist.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_mediacrypto.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_mediadrm.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_mediaerror.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_mediaextractor.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_mediaformat.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_mediaplayer.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_musicservice.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_perception_client.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_privileges.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_screens.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_secure_storage.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_sharedfile.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/ml_virtual_device.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/OrientationMixer.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/PassthroughMixer.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/portaudio_x64.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/PositionMixer.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/protobuf-cpp-full.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/z.dll',
                    '<(module_root_dir)/node_modules/magicleap/lib/win64/zmq.dll',
                  ],
                }
              ],
              'defines': [
                'MAGICLEAP=$(MAGICLEAP)',
              ],
            }],
          ],
        }],
        ['OS=="linux"', {
          'sources': [
            'main.cpp',
            '<!@(ls -1 deps/exokit-bindings/bindings/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/util/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/canvas/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/nanosvg/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/canvascontext/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webglcontext/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webaudiocontext/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/videocontext/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/glfw/src/*.cc)',
            '<!@(ls -1 deps/openvr/src/*.cpp)',
          ],
          'include_dirs': [
            '<(module_root_dir)/node_modules/native-graphics-deps/include',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/core',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/config',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/gpu',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/effects',
            '<(module_root_dir)/node_modules/native-audio-deps/include',
            '<(module_root_dir)/node_modules/native-video-deps/include',
            '<(module_root_dir)/node_modules/native-openvr-deps/headers',
            '<(module_root_dir)/deps/exokit-bindings',
            '<(module_root_dir)/deps/exokit-bindings/utf8',
            '<(module_root_dir)/deps/exokit-bindings/node',
            '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
            '<(module_root_dir)/deps/exokit-bindings/util/include',
            '<(module_root_dir)/deps/exokit-bindings/bindings/include',
            '<(module_root_dir)/deps/exokit-bindings/canvas/include',
            '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
            '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/glfw/include',
            '<(module_root_dir)/deps/openvr/include',
          ],
          'library_dirs': [
            '<(module_root_dir)/node_modules/native-graphics-deps/lib/linux/glew',
            '<(module_root_dir)/node_modules/native-graphics-deps/lib/linux/glfw',
            '<(module_root_dir)/node_modules/native-canvas-deps/lib/linux',
            '<(module_root_dir)/node_modules/native-audio-deps/lib/linux',
            '<(module_root_dir)/node_modules/native-video-deps/lib/linux',
            '<(module_root_dir)/node_modules/native-video-deps/lib/linux/libavformat',
            '<(module_root_dir)/node_modules/native-video-deps/lib/linux/libavcodec',
            '<(module_root_dir)/node_modules/native-video-deps/lib/linux/libavutil',
            '<(module_root_dir)/node_modules/native-video-deps/lib/linux/libswscale',
            '<(module_root_dir)/node_modules/native-video-deps/lib/linux/libswresample',
            '<(module_root_dir)/node_modules/native-openvr-deps/lib/linux64',
          ],
          'libraries': [
            '-lGL',
            '-lGLU',
            '-lX11',
            '-lGLEW',
            '-lglfw3',
            '-lfontconfig',
            '-lfreetype',
            '-lpng16',
            '-lskia',
            '-lLabSound',
            '-lavformat',
            '-lavcodec',
            '-lavutil',
            '-lswscale',
            '-lswresample',
            '-lopenvr_api',
            '-luuid',
          ],
          'ldflags': [
            '-Wl,-Bsymbolic', # required for ffmpeg asm linkage
            '-Wl,--no-as-needed', # required to prevent elision of shared object linkage
            '-Wl,-rpath,./node_modules/native-graphics-deps/lib/linux/glew',
            '-Wl,-rpath,./node_modules/native-graphics-deps/lib/linux/glfw',
            '-Wl,-rpath,./node_modules/native-canvas-deps/lib/linux',
            '-Wl,-rpath,./node_modules/native-audio-deps/lib/linux',
            '-Wl,-rpath,./node_modules/native-video-deps/lib/linux/libavformat',
            '-Wl,-rpath,./node_modules/native-video-deps/lib/linux/libavcodec',
            '-Wl,-rpath,./node_modules/native-video-deps/lib/linux/libavutil',
            '-Wl,-rpath,./node_modules/native-video-deps/lib/linux/libswscale',
            '-Wl,-rpath,./node_modules/native-video-deps/lib/linux/libswresample',
            '-Wl,-rpath,./node_modules/native-openvr-deps/bin/linux64',
          ],
          'defines': [
            'NOMINMAX',
          ],
        }],
        ['OS=="mac"', {
          'sources': [
            'main.cpp',
            '<!@(ls -1 deps/exokit-bindings/bindings/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/util/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/canvas/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/nanosvg/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/canvascontext/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webglcontext/src/*.cc)',
            '<!@(ls -1 deps/exokit-bindings/webaudiocontext/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/videocontext/src/*.cpp)',
            '<!@(ls -1 deps/exokit-bindings/glfw/src/*.cc)',
            '<!@(ls -1 deps/openvr/src/*.cpp)',
          ],
          'include_dirs': [
            '<(module_root_dir)/node_modules/native-graphics-deps/include',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/core',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/config',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/gpu',
            '<(module_root_dir)/node_modules/native-canvas-deps/include/effects',
            '<(module_root_dir)/node_modules/native-audio-deps/include',
            '<(module_root_dir)/node_modules/native-video-deps/include',
            '<(module_root_dir)/node_modules/native-openvr-deps/headers',
            '<(module_root_dir)/deps/exokit-bindings',
            '<(module_root_dir)/deps/exokit-bindings/utf8',
            '<(module_root_dir)/deps/exokit-bindings/node',
            '<(module_root_dir)/deps/exokit-bindings/native_app_glue',
            '<(module_root_dir)/deps/exokit-bindings/util/include',
            '<(module_root_dir)/deps/exokit-bindings/bindings/include',
            '<(module_root_dir)/deps/exokit-bindings/canvas/include',
            '<(module_root_dir)/deps/exokit-bindings/nanosvg/include',
            '<(module_root_dir)/deps/exokit-bindings/canvascontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webglcontext/include',
            '<(module_root_dir)/deps/exokit-bindings/webaudiocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/videocontext/include',
            '<(module_root_dir)/deps/exokit-bindings/glfw/include',
            '<(module_root_dir)/deps/openvr/include',
          ],
          'library_dirs': [
            '<(module_root_dir)/node_modules/native-graphics-deps/lib/macos/glew',
            '<(module_root_dir)/node_modules/native-graphics-deps/lib/macos/glfw',
            '<(module_root_dir)/node_modules/native-canvas-deps/lib/macos',
            '<(module_root_dir)/node_modules/native-audio-deps/lib/macos',
            '<(module_root_dir)/node_modules/native-video-deps/lib/macos',
          ],
          'libraries': [
            '-framework OpenGL',
            '-framework Cocoa',
            '-lGLEW',
            '-lglfw3',
            '-lskia',
            '-framework CoreAudio',
            '-framework AudioUnit',
            '-framework AudioToolbox',
            '-llabsound',
            '-lavformat',
            '-lavcodec',
            '-lavutil',
            '-lswscale',
            '-lswresample',
            '-F <(module_root_dir)/node_modules/native-openvr-deps/bin/osx64',
            '-framework OpenVR',
          ],
          'link_settings': {
            'libraries': [
              '-Wl,-rpath,./node_modules/native-audio-deps/lib/macos',
              '-Wl,-rpath,./node_modules/native-video-deps/lib/macos',
              '-Wl,-rpath,./node_modules/native-openvr-deps/bin/osx64',
              '-framework OpenVR',
            ],
          },
        }],
      ],
    },
  ],
}
