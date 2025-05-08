

##############################################

import torch
import torch_xla
import torch_xla.core.xla_model as xm

try:
    if (xm.xla_device().type == 'xla'):
        print("Yes XLA TPU :)")
        print(f"Version of Python: {sys.version.split()[0]}")
        print(f"Version of PyTorch: {torch.__version__}")
        print(f"Version of XLA TPU: {torch_xla.__version__}")
        print(f"# of XLA TPU Cores: {len(xm.get_xla_supported_devices())}")
        print(f"Current Index of XLA TPU: {xm.xla_device()}")
    else:
        pass
except:
    print("No XLA TPU :(")


try:
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver(tpu='local')
    if not hasattr(tf.tpu, 'experimental') or not getattr(tf.tpu.experimental, '_tpu_initialized', False):
        tf.config.experimental_connect_to_cluster(resolver)
        tf.tpu.experimental.initialize_tpu_system(resolver)
        setattr(tf.tpu.experimental, '_tpu_initialized', True)
    if tf.config.list_physical_devices('TPU'):
        print("Yes TPU :)")
        print(f"Version of Python: {sys.version.split()[0]}")
        print(f"Version of TensorFlow: {tf.__version__}")
        print(f"# of TPU Cores: {len(tf.config.list_physical_devices('TPU'))}")
        print(f"Current Device of TPU: {tf.config.list_logical_devices('TPU')[0].name}")
    else:
        pass
except:
    print("No TPU :(")


##############################################

!pip install torch-xla 

# Try these methods to get TPU device information
import torch_xla.core.xla_model as xm

try:
    # Method 1: Get XLA supported devices
    ldevices = xm.get_xla_supported_devices()
    print("XLA Supported Devices:", ldevices)
    
    # Method 2: Try to get device
    device = xm.xla_device()
    print("XLA Device:", device)
except Exception as e:
    print("Error getting TPU devices:", e)
    
##############################################

import tensorflow as tf

# TPUデバイスの検出
try:
    resolver = tf.distribute.cluster_resolver.TPUClusterResolver()  # TPUの解決
    tf.config.experimental_connect_to_cluster(resolver)  # TPUに接続
    tf.config.experimental_initialize_system()  # システムの初期化
    strategy = tf.distribute.TPUStrategy(resolver)  # TPU戦略
    print("TPU devices:", resolver.cluster_spec().as_dict())
except ValueError:
    strategy = tf.distribute.get_strategy()  # TPUが使えない場合はCPU/GPU戦略
    print("Using default strategy (CPU or GPU)")

# TPUを使ってモデルを訓練する
with strategy.scope():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(784,)),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# モデルの訓練（例）
# model.fit(train_dataset, epochs=5)


##############################################

def get_strategy(device='TPU'):
    if "TPU" in device:
        tpu = 'local' if device=='TPU-VM' else None
        print("connecting to TPU...")
        tpu = tf.distribute.cluster_resolver.TPUClusterResolver.connect(tpu=tpu)
        strategy = tf.distribute.TPUStrategy(tpu)
        IS_TPU = True

    if device == "GPU"  or device=="CPU":
        ngpu = len(tf.config.experimental.list_physical_devices('GPU'))
        if ngpu>1:
            print("Using multi GPU")
            strategy = tf.distribute.MirroredStrategy()
        elif ngpu==1:
            print("Using single GPU")
            strategy = tf.distribute.get_strategy()
        else:
            print("Using CPU")
            strategy = tf.distribute.get_strategy()
        IS_TPU = False

    if device == "GPU":
        print("Num GPUs Available: ", ngpu)

    AUTO     = tf.data.experimental.AUTOTUNE
    REPLICAS = strategy.num_replicas_in_sync
    print(f'REPLICAS: {REPLICAS}')

    return strategy, REPLICAS, IS_TPU

STRATEGY, N_REPLICAS, IS_TPU = get_strategy('TPU-VM')

##############################################

import tensorflow as tf
try:
    tpu = tf.distribute.cluster_resolver.TPUClusterResolver()
    print('Device:', tpu.master())
    tf.config.experimental_connect_to_cluster(tpu)
    tf.tpu.experimental.initialize_tpu_system(tpu)
    strategy = tf.distribute.experimental.TPUStrategy(tpu)
except:
    strategy = tf.distribute.get_strategy()
print('Number of replicas:', strategy.num_replicas_in_sync)

##############################################
