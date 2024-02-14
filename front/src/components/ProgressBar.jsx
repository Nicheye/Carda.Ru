import React, { useRef, useEffect, useState } from 'react';

const ProgressBar = ({ value, goal }) => {
  const progressRef = useRef(null);
  const [progressWidth, setProgressWidth] = useState(0);

  useEffect(() => {
    if (progressRef.current) {
      const rect = progressRef.current.getBoundingClientRect();
      setProgressWidth(rect.width-70);
    }
  }, [value]);

  return (
    <div className="progress-bar" ref={progressRef}>
      <div className="progress" style={{ width: `${value}%` }}></div>
      <div className="progress-goal" style={{ width: progressWidth }}>{goal}</div>
    </div>
  );
};

export default ProgressBar;
