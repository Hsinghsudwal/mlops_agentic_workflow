import argparse
from orchestrator.agentic_orchestrator import AgenticOrchestrator


def main():
    parser = argparse.ArgumentParser("Agentic Data Runtime")

    parser.add_argument(
        "--phase",
        required=True,
        help="Choose agent"
    )

    parser.add_argument("--cost", type=float, default=10.0)

    parser.add_argument(
        "--dataset",
        required=True,
        help="Dataset-path"
    )
    
    args = parser.parse_args()
    
    orchestrator = AgenticOrchestrator(
        phase=args.phase,
        dataset=args.dataset,
        cost=args.cost,

    )
    
    result = orchestrator.run()
    
    if result["success"]:
        print(f"Execution completed: {result['summary']}")
    else:
        print(f"Execution failed: {result['error']}")
        exit(1)


if __name__ == "__main__":
    main()
