# -*- coding: utf-8 -*-

# Copyright 2018, IBM.
#
# This source code is licensed under the Apache License, Version 2.0 found in
# the LICENSE.txt file in the root directory of this source tree.

"""DEPRECATED: WILL BE REMOVED AFTER 0.8."""
import warnings
import logging

from qiskit.compiler.transpiler import transpile
from qiskit.compiler.assembler import assemble

logger = logging.getLogger(__name__)


# pylint: disable=redefined-builtin
def compile(circuits, backend,
            config=None, basis_gates=None, coupling_map=None, initial_layout=None,
            shots=1024, max_credits=10, seed=None, qobj_id=None, seed_mapper=None,
            pass_manager=None, memory=False):
    """Compile a list of circuits into a qobj.

    Args:
        circuits (QuantumCircuit or list[QuantumCircuit]): circuits to compile
        backend (BaseBackend): a backend to compile for
        config (dict): dictionary of parameters (e.g. noise) used by runner
        basis_gates (list[str]): list of basis gates names supported by the
            target. Default: ['u1','u2','u3','cx','id']
        coupling_map (list): coupling map (perhaps custom) to target in mapping
        initial_layout (list): initial layout of qubits in mapping
        shots (int): number of repetitions of each circuit, for sampling
        max_credits (int): maximum credits to use
        seed (int): random seed for simulators
        seed_mapper (int): random seed for swapper mapper
        qobj_id (int): identifier for the generated qobj
        pass_manager (PassManager): a pass manger for the transpiler pipeline
        memory (bool): if True, per-shot measurement bitstrings are returned as well

    Returns:
        Qobj: the qobj to be run on the backends

    Raises:
        QiskitError: if the desired options are not supported by backend
    """
    warnings.warn('qiskit.compile() is deprecated and will be removed in Qiskit Terra 0.9. '
                  'Please use qiskit.compiler.transpile() to transform circuits '
                  'and qiskit.compiler.assemble() to produce a runnable qobj.',
                  DeprecationWarning)

    new_circuits = transpile(circuits,
                             basis_gates=basis_gates,
                             coupling_map=coupling_map,
                             initial_layout=initial_layout,
                             seed_transpiler=seed_mapper,
                             backend=backend,
                             pass_manager=pass_manager)

    qobj = assemble(new_circuits,
                    qobj_header=None,
                    shots=shots,
                    max_credits=max_credits,
                    seed_simulator=seed,
                    memory=memory,
                    qobj_id=qobj_id,
                    config=config)  # deprecated

    return qobj
