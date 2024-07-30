import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Vote: React.FC = () => {
  const [candidates, setCandidates] = useState([]);

  useEffect(() => {
    const fetchCandidates = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/candidates/');
        setCandidates(response.data);
      } catch (error) {
        console.error('Error fetching candidates', error);
      }
    };

    fetchCandidates();
  }, []);

  const handleVote = async (candidateId: number) => {
    try {
      const token = localStorage.getItem('token');
      await axios.post(
        'http://127.0.0.1:8000/api/votes/',
        { candidate: candidateId },
        {
          headers: {
            Authorization: `Bearer ${token}`,
          },
        }
      );
      // Show success message or update UI
    } catch (error) {
      console.error('Error casting vote', error);
    }
  };

  return (
    <div className="max-w-lg mx-auto mt-10">
      <h1 className="text-2xl font-bold mb-6">Vote for Your Candidates</h1>
      <ul className="space-y-4">
        {candidates.map((candidate: any) => (
          <li key={candidate.id} className="bg-white shadow-md rounded p-4 flex justify-between items-center">
            <h2 className="text-lg font-medium">{candidate.full_name}</h2>
            <button
              onClick={() => handleVote(candidate.id)}
              className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            >
              Vote
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Vote;
