kmeans_params = {
    'n_clusters': {
        'type': 'categorical',
        'values': [2, 3, 4]
    },
    'init': {
        'type': 'categorical',
        'values': ['k-means++', 'random']
    },
    'n_init': {
        'type': 'int',
        'low': 5,
        'high': 20
    },
    'random_state': {
        'type': 'categorical',
        'values': [42]
    }
}

dbscan_params = {
    'eps': {
        'type': 'float',
        'low': 0.01,
        'high': 2.0,
        'step': 0.01
    },
    'min_samples': {
        'type': 'int',
        'low': 2,
        'high': 20
    },
    'n_jobs': {
        'type': 'categorical',
        'values': [-1]
    }
}

gmm_params = {
    'n_components': {
        'type': 'categorical',
        'values': [2, 3, 4, 5, 6]
    },
    'covariance_type': {
        'type': 'categorical',
        'values': ['full', 'tied', 'diag', 'spherical']
    },
    'random_state': {
        'type': 'categorical',
        'values': [42]
    }
}

agglomerative_params = {
    'n_clusters': {
        'type': 'categorical',
        'values': [2, 3, 4]
    },
    'linkage': {
        'type': 'categorical',
        'values': ['ward', 'complete', 'average', 'single']
    }
}

affinity_propagation_params = {
    'damping': {
        'type': 'float',
        'low': 0.5,
        'high': 0.99,
        'step': 0.01
    },
    'random_state': {
        'type': 'categorical',
        'values': [42]
    }
}
