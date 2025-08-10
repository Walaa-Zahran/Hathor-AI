type Action = {
  type: string;
  score: number;
};

export function validateAction(action: Action): boolean {
  // Example: only allow if score >= 70
  if (action.score >= 70) {
    return true;
  }
  return false;
}

// Example usage:
const testAction = { type: "LEND", score: 80 };
console.log("Action allowed:", validateAction(testAction));
